import os
from datetime import datetime

import pytest
import requests_mock

from jungle_scout.client import Client
from jungle_scout.models.parameters import Marketplace
from jungle_scout.models.responses.keyword_by_asin import KeywordByASIN

from .factories.keyword_by_asin_factory import generate_keywords_by_asin_responses


@pytest.fixture
def client():
    return Client(api_key_name=os.environ["API_KEY_NAME"], api_key=os.environ["API_KEY"], marketplace=Marketplace.US)


@pytest.mark.parametrize(
    "asin, fake_response",
    [
        ("B005IHSKYS", generate_keywords_by_asin_responses(1)),
        (
            ["B005IHSKYS", "B0CL5KNB9M", "B005IHSKYS", "B0CL5KNB9M", "B005IHSKYS"],
            generate_keywords_by_asin_responses(5),
        ),
        (
            [
                "B005IHSKYS",
                "B0CL5KNB9M",
                "B005IHSKYS",
                "B0CL5KNB9M",
                "B005IHSKYS",
                "B0CL5KNB9M",
                "B005IHSKYS",
                "B0CL5KNB9M",
                "B005IHSKYS",
                "B0CL5KNB9M",
            ],
            generate_keywords_by_asin_responses(10),
        ),
    ],
)
def test_keywords_by_asin(client, asin, fake_response):
    with requests_mock.Mocker() as mock:
        mock_url = f"{client.session.base_url}/keywords/keywords_by_asin_query"
        mock.post(
            mock_url,
            json={"data": fake_response},
        )

        result = client.keywords_by_asin(asin=asin)

    assert mock.called
    assert mock.call_count == 1

    history = mock.request_history
    assert len(history) == 1
    assert history[0].url == f"{mock_url}?marketplace=us"
    assert history[0].query == "marketplace=us"
    assert history[0].method == "POST"
    assert history[0].json() == {
        "data": {
            "type": "keywords_by_asin_query",
            "attributes": {"asins": [asin] if isinstance(asin, str) else asin, "include_variants": True},
        }
    }
    assert len(result) == len(history[0].json()["data"]["attributes"]["asins"])

    assert len(result) == len(fake_response)
    assert isinstance(result[0], KeywordByASIN)
    assert result[0].data_type == fake_response[0]["type"]
    assert result[0].id == fake_response[0]["id"]
    assert isinstance(result[0].updated_at, datetime)
