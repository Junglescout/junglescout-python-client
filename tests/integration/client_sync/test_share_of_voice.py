import pytest
from httpx import HTTPStatusError

from junglescout import ClientSync
from junglescout.exceptions import JungleScoutHTTPError
from junglescout.models.parameters import Marketplace
from junglescout.models.responses import ShareOfVoiceTopAsins


@pytest.mark.integration()
def test_share_of_voice(api_keys):
    keyword = "yoga mat"
    client = ClientSync(**api_keys, marketplace=Marketplace.US)
    response = client.share_of_voice(keyword=keyword, marketplace=Marketplace.US)
    client.close()
    assert client.is_closed
    assert response.data is not None
    assert response.data.type == "share_of_voice"
    assert response.data.id == f"us/{keyword}"
    assert response.data.attributes.estimated_30_day_search_volume > 0
    assert isinstance(response.data.attributes.brands[0].brand, str)
    assert isinstance(response.data.attributes.top_asins[0], ShareOfVoiceTopAsins)


@pytest.mark.integration()
def test_share_of_voice_with_long_keyword(api_keys):
    keyword = "this is a super long keyword that will raise an error because it is too long and specific"
    client = ClientSync(**api_keys, marketplace=Marketplace.US)
    with pytest.raises(JungleScoutHTTPError) as exc_info:
        client.share_of_voice(keyword=keyword, marketplace=Marketplace.US)
    client.close()
    assert client.is_closed
    assert isinstance(exc_info.value.httpx_exception, HTTPStatusError)
    assert exc_info.value.httpx_exception.response.json() == {
        "errors": [
            {
                "title": "Invalid parameter value for: 'keyword'",
                "detail": "keyword - is too long (maximum is 50 characters)",
                "code": "VALIDATION_ERROR",
                "source": {"pointer": "/data/attributes/keyword"},
                "status": "422",
            }
        ]
    }


@pytest.mark.integration()
def test_share_of_voice_with_no_results(api_keys):
    keyword = "thisisnotarealkeywordthisisnotarealkeywordthisisno"
    client = ClientSync(**api_keys, marketplace=Marketplace.US)
    with pytest.raises(JungleScoutHTTPError) as exc_info:
        client.share_of_voice(keyword=keyword, marketplace=Marketplace.US)
    client.close()
    assert client.is_closed
    assert isinstance(exc_info.value.httpx_exception, HTTPStatusError)
    assert exc_info.value.httpx_exception.response.json() == {
        "errors": [
            {
                "title": "Record not found",
                "detail": (
                    f"There doesn't seem to be any Sponsored or Organic Data for this keyword (us/{keyword}). "
                    "Please try a different keyword to find Sponsored or Organic Data."
                ),
                "code": "RECORD_NOT_FOUND",
                "status": "404",
            }
        ]
    }
