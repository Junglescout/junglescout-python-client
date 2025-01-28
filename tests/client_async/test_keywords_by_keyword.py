import json

import httpx
import pytest
import respx

from junglescout.models.parameters import Marketplace, Sort
from junglescout.models.responses import APIResponse, KeywordByKeyword
from tests.factories.keywords_by_keyword_factory import (
    generate_keywords_by_keyword_responses,
)


@pytest.mark.parametrize(
    ("search_terms", "fake_response"),
    [
        ("yoga", generate_keywords_by_keyword_responses(total_items=1)),
        ("yoga_mat", generate_keywords_by_keyword_responses(total_items=4)),
    ],
)
@respx.mock
@pytest.mark.asyncio
async def test_keywords_by_keywords(client_async, search_terms, fake_response):
    mock_url = f"{client_async.session.base_url}/keywords/keywords_by_keyword_query"
    mock_route = respx.post(mock_url).mock(return_value=httpx.Response(200, json=fake_response))
    result = await client_async.keywords_by_keyword(search_terms=search_terms)

    assert mock_route.called
    assert mock_route.call_count == 1

    request: httpx.Request = mock_route.calls[0].request
    assert str(request.url.copy_with(query=None)) == mock_url
    assert str(request.url.params) == "marketplace=us"
    assert request.method == "POST"

    request_content = json.loads(request.content)
    assert request_content == {
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
    assert result.meta.model_dump() == {"total_items": len(fake_response["data"]), "errors": None}
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
@respx.mock
@pytest.mark.asyncio
async def test_keywords_by_keywords_headers(client_async, search_terms, sort_options, fake_response):
    mock_url = f"{client_async.session.base_url}/keywords/keywords_by_keyword_query"
    mock_route = respx.post(mock_url).mock(return_value=httpx.Response(200, json=fake_response))
    result = await client_async.keywords_by_keyword(search_terms=search_terms, sort_option=sort_options)

    assert mock_route.called
    assert mock_route.call_count == 1

    request: httpx.Request = mock_route.calls[0].request
    assert str(request.url.copy_with(query=None)) == mock_url
    assert str(request.url.params) == f"marketplace=us&sort={sort_options.value}"
    assert request.method == "POST"

    request_content = json.loads(request.content)
    assert request_content == {
        "data": {
            "type": "keywords_by_keyword_query",
            "attributes": {"search_terms": search_terms, "categories": Marketplace.US.categories},
        }
    }

    assert len(result.data) == len(fake_response["data"])
    assert isinstance(result, APIResponse)
