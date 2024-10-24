import json
import os
from datetime import datetime

import httpx
import pytest
import respx

from junglescout import Client
from junglescout.models.parameters import Marketplace
from junglescout.models.responses import APIResponse, KeywordByASIN
from tests.factories.keyword_by_asin_factory import generate_keywords_by_asin_responses


@pytest.fixture()
def client():
    return Client(api_key_name=os.environ["API_KEY_NAME"], api_key=os.environ["API_KEY"], marketplace=Marketplace.US)


@pytest.mark.parametrize(
    ("asin", "fake_response"),
    [
        ("B005IHSKYS", generate_keywords_by_asin_responses(total_items=1)),
        (
            ["B005IHSKYS", "B0CL5KNB9M", "B005IHSKYS", "B0CL5KNB9M", "B005IHSKYS"],
            generate_keywords_by_asin_responses(total_items=5),
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
            generate_keywords_by_asin_responses(total_items=10),
        ),
    ],
)
@respx.mock
def test_keywords_by_asin(client, asin, fake_response):
    mock_url = f"{client.session.base_url}/keywords/keywords_by_asin_query"
    # TODO: what's the response code here????
    mock_route = respx.post(mock_url).mock(return_value=httpx.Response(200, json=fake_response))
    result = client.keywords_by_asin(asin=asin)

    assert mock_route.called
    assert mock_route.call_count == 1

    request: httpx.Request = mock_route.calls[0].request
    assert str(request.url.copy_with(query=None)) == mock_url
    assert str(request.url.params) == "marketplace=us"
    assert request.method == "POST"

    request_content = json.loads(request.content)
    assert request_content == {
        "data": {
            "type": "keywords_by_asin_query",
            "attributes": {"asins": [asin] if isinstance(asin, str) else asin, "include_variants": True},
        }
    }
    assert len(result.data) == len(request_content["data"]["attributes"]["asins"])

    assert len(result.data) == len(fake_response["data"])
    assert isinstance(result, APIResponse)
    assert isinstance(result.data[0], KeywordByASIN)
    assert result.data[0].type == fake_response["data"][0]["type"]
    assert result.data[0].id == fake_response["data"][0]["id"]
    assert isinstance(result.data[0].attributes.updated_at, datetime)
    assert result.data[0].model_dump() == fake_response["data"][0]
