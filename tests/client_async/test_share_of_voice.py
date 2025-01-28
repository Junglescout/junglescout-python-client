import httpx
import pytest
import respx

from junglescout.models.parameters import Marketplace
from tests.factories.share_of_voice_factory import generate_share_of_voice_responses


@pytest.mark.parametrize(
    ("keyword", "marketplace", "fake_response"),
    [
        ("yoga", Marketplace.CA, generate_share_of_voice_responses()),
        ("ps5", Marketplace.US, generate_share_of_voice_responses()),
    ],
)
@respx.mock
@pytest.mark.asyncio()
async def test_share_of_voice(client_async, keyword, marketplace, fake_response):
    mock_url = f"{client_async.session.base_url}/share_of_voice"
    mock_route = respx.get(mock_url).mock(return_value=httpx.Response(200, json=fake_response))
    result = await client_async.share_of_voice(keyword=keyword, marketplace=marketplace)

    assert mock_route.called
    assert mock_route.call_count == 1

    request: httpx.Request = mock_route.calls[0].request
    assert str(request.url.copy_with(query=None)) == mock_url
    assert str(request.url.params) == f"marketplace={marketplace.country_code}&page%5Bsize%5D=50&keyword={keyword}"
    assert request.method == "GET"

    assert result.data.attributes.model_dump() == fake_response["data"]["attributes"]
