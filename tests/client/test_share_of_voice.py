import os

import pytest
import requests_mock

from jungle_scout.client import Client
from jungle_scout.models.parameters import Marketplace
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
def test_share_of_voice(client, keyword, marketplace, fake_response):
    with requests_mock.Mocker() as mock:
        mock_url = f"{client.session.base_url}/share_of_voice"
        mock.get(
            mock_url,
            json=fake_response,
        )

        result = client.share_of_voice(keyword=keyword, marketplace=marketplace)

    assert mock.called
    assert mock.call_count == 1

    history = mock.request_history
    assert len(history) == 1
    assert history[0].url == f"{mock_url}?marketplace={marketplace.country_code}&page%5Bsize%5D=50&keyword={keyword}"
    assert history[0].query == f"marketplace={marketplace.country_code}&page%5bsize%5d=50&keyword={keyword}"
    assert history[0].method == "GET"

    assert result.data.attributes.model_dump() == fake_response["data"]["attributes"]
