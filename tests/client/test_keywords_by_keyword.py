import os

import pytest
import requests_mock

from jungle_scout.client import Client
from jungle_scout.models.parameters import Marketplace, Sort
from jungle_scout.models.responses import APIResponse, KeywordByKeyword
from tests.factories.keywords_by_keyword_factory import (
    generate_keywords_by_keyword_responses,
)


@pytest.fixture()
def client():
    return Client(api_key_name=os.environ["API_KEY_NAME"], api_key=os.environ["API_KEY"], marketplace=Marketplace.US)


@pytest.mark.parametrize(
    ("search_terms", "fake_response"),
    [
        ("yoga", generate_keywords_by_keyword_responses(total_items=1)),
        ("yoga_mat", generate_keywords_by_keyword_responses(total_items=4)),
    ],
)
def test_keywords_by_keywords(client, search_terms, fake_response):
    with requests_mock.Mocker() as mock:
        mock_url = f"{client.session.base_url}/keywords/keywords_by_keyword_query"
        mock.post(
            mock_url,
            json=fake_response,
        )

        result = client.keywords_by_keyword(search_terms=search_terms)

    assert mock.called
    assert mock.call_count == 1

    history = mock.request_history

    assert len(history) == 1
    assert history[0].url == f"{mock_url}?marketplace=us"
    assert history[0].query == "marketplace=us"
    assert history[0].method == "POST"
    assert history[0].json() == {
        "data": {
            "type": "keywords_by_keyword_query",
            "attributes": {"search_terms": search_terms, "categories": Marketplace.US.categories},
        }
    }

    assert len(result.data) == len(fake_response["data"])
    assert isinstance(result, APIResponse)
    assert isinstance(result.data[0], KeywordByKeyword)
    assert result.data[0].type == fake_response["data"][0]["type"]
    assert result.data[0].id == fake_response["data"][0]["id"]
    assert result.links.model_dump() == fake_response["links"]
    assert result.meta.model_dump() == fake_response["meta"]
    assert result.data[0].attributes.model_dump() == fake_response["data"][0]["attributes"]


@pytest.mark.parametrize(
    ("search_terms", "sort_options", "fake_response"),
    [
        (
            "yoga",
            Sort.MONTHLY_TREND,
            generate_keywords_by_keyword_responses(total_items=1),
        ),
        (
            "yoga mat",
            Sort.MONTHLY_TREND,
            generate_keywords_by_keyword_responses(total_items=3),
        ),
    ],
)
def test_keywords_by_keywords_headers(client, search_terms, sort_options, fake_response):
    with requests_mock.Mocker() as mock:
        mock_url = f"{client.session.base_url}/keywords/keywords_by_keyword_query"
        mock.post(
            mock_url,
            json=fake_response,
        )

        result = client.keywords_by_keyword(search_terms=search_terms, sort_option=sort_options)

    assert mock.called
    assert mock.call_count == 1

    history = mock.request_history

    assert len(history) == 1
    assert history[0].url == f"{mock_url}?marketplace=us&sort={sort_options.value}"
    assert history[0].query == f"marketplace=us&sort={sort_options.value}"
    assert history[0].method == "POST"
    assert history[0].json() == {
        "data": {
            "type": "keywords_by_keyword_query",
            "attributes": {"search_terms": search_terms, "categories": Marketplace.US.categories},
        }
    }

    assert len(result.data) == len(fake_response["data"])
    assert isinstance(result, APIResponse)
