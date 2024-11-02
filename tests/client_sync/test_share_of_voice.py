import os

import httpx
import pytest
import respx

from junglescout import Client
from junglescout.models.parameters import Marketplace
from tests.factories.share_of_voice_factory import generate_share_of_voice_responses


@pytest.fixture()
def client():
    return Client(api_key_name=os.environ["API_KEY_NAME"], api_key=os.environ["API_KEY"], marketplace=Marketplace.US)


@pytest.mark.parametrize(
    ("keyword", "marketplace", "fake_response"),
    [
        ("yoga", Marketplace.CA, generate_share_of_voice_responses()),
        ("ps5", Marketplace.US, generate_share_of_voice_responses()),
    ],
)
@respx.mock
def test_share_of_voice(client, keyword, marketplace, fake_response):
    mock_url = f"{client.session.base_url}/share_of_voice"
    mock_route = respx.get(mock_url).mock(return_value=httpx.Response(200, json=fake_response))
    result = client.share_of_voice(keyword=keyword, marketplace=marketplace)

    assert mock_route.called
    assert mock_route.call_count == 1

    request: httpx.Request = mock_route.calls[0].request
    assert str(request.url.copy_with(query=None)) == mock_url
    assert str(request.url.params) == f"marketplace={marketplace.country_code}&page%5Bsize%5D=50&keyword={keyword}"
    assert request.method == "GET"

    assert result.data.attributes.model_dump() == fake_response["data"]["attributes"]
