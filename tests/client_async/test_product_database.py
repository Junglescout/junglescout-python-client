import json
from datetime import datetime

import httpx
import pytest
import respx

from junglescout.models.parameters import (
    Marketplace,
    ProductFilterOptions,
    ProductSort,
    ProductTiers,
    SellerTypes,
)
from junglescout.models.responses import APIResponse, ProductDatabase
from tests.factories.product_database_factory import generate_product_database_responses


@pytest.mark.parametrize(
    ("include_keywords", "exclude_keywords", "fake_response"),
    [
        (["yoga", "gym"], ["bath"], generate_product_database_responses(total_items=1)),
        (["yoga_mat", "mat", "yoga accessories"], ["floor mat"], generate_product_database_responses(total_items=10)),
    ],
)
@respx.mock
@pytest.mark.asyncio()
async def test_product_database(client_async, include_keywords, exclude_keywords, fake_response):
    mock_url = f"{client_async.session.base_url}/product_database_query"
    mock_route = respx.post(mock_url).mock(return_value=httpx.Response(200, json=fake_response))
    result = await client_async.product_database(include_keywords=include_keywords, exclude_keywords=exclude_keywords)

    assert mock_route.called
    assert mock_route.call_count == 1

    request: httpx.Request = mock_route.calls[0].request
    assert str(request.url.copy_with(query=None)) == mock_url
    assert str(request.url.params) == "marketplace=us&page%5Bsize%5D=10"
    assert request.method == "POST"

    request_content = json.loads(request.content)
    assert request_content == {
        "data": {
            "type": "product_database_query",
            "attributes": {
                "include_keywords": include_keywords,
                "exclude_keywords": exclude_keywords,
                "categories": Marketplace.US.categories,
                "product_tiers": [ProductTiers.OVERSIZE.value, ProductTiers.STANDARD.value],
                "seller_types": [SellerTypes.AMZ.value, SellerTypes.FBA.value, SellerTypes.FBM.value],
            },
        }
    }

    assert len(result.data) == len(fake_response["data"])
    assert isinstance(result, APIResponse)
    assert isinstance(result.data[0], ProductDatabase)
    assert result.data[0].type == fake_response["data"][0]["type"]
    assert result.data[0].id == fake_response["data"][0]["id"]
    assert result.links.model_dump() == fake_response["links"]
    assert result.meta.model_dump() == {"errors": None, "total_items": len(fake_response["data"])}
    assert result.data[0].attributes.seller_type == fake_response["data"][0]["attributes"]["seller_type"]
    assert (
        result.data[0].attributes.fee_breakdown.model_dump() == fake_response["data"][0]["attributes"]["fee_breakdown"]
    )
    assert isinstance(result.data[0].attributes.updated_at, datetime)
    assert result.data[0].model_dump() == fake_response["data"][0]


@pytest.mark.parametrize(
    (
        "include_keywords",
        "exclude_keywords",
        "page_size",
        "product_filter_options",
        "seller_types",
        "product_tiers",
        "product_sort_option",
        "fake_response",
    ),
    [
        (
            ["yoga", "gym"],
            ["bath"],
            5,
            ProductFilterOptions(min_price=100),
            [SellerTypes.AMZ.value],
            [ProductTiers.STANDARD.value],
            ProductSort.NAME.value,
            generate_product_database_responses(total_items=4),
        ),
    ],
)
@respx.mock
@pytest.mark.asyncio()
async def test_full_request_product_database(
    client_async,
    include_keywords,
    exclude_keywords,
    page_size,
    product_filter_options,
    seller_types,
    product_tiers,
    product_sort_option,
    fake_response,
):
    mock_url = f"{client_async.session.base_url}/product_database_query"
    mock_route = respx.post(mock_url).mock(return_value=httpx.Response(200, json=fake_response))
    result = await client_async.product_database(
        include_keywords=include_keywords,
        exclude_keywords=exclude_keywords,
        page_size=page_size,
        product_filter_options=product_filter_options,
        seller_types=seller_types,
        product_tiers=product_tiers,
        product_sort_option=product_sort_option,
    )

    assert mock_route.called
    assert mock_route.call_count == 1

    request: httpx.Request = mock_route.calls[0].request
    assert str(request.url.copy_with(query=None)) == mock_url
    assert str(request.url.params) == "marketplace=us&page%5Bsize%5D=5&product_sort_option=-name"
    assert request.method == "POST"

    request_content = json.loads(request.content)
    assert request_content == {
        "data": {
            "type": "product_database_query",
            "attributes": {
                "include_keywords": include_keywords,
                "exclude_keywords": exclude_keywords,
                "categories": Marketplace.US.categories,
                "product_tiers": [ProductTiers.STANDARD.value],
                "seller_types": [SellerTypes.AMZ.value],
                "min_price": 100,
            },
        }
    }

    assert len(result.data) == len(fake_response["data"])
    assert isinstance(result, APIResponse)
    assert isinstance(result.data[0], ProductDatabase)
    assert result.data[0].type == fake_response["data"][0]["type"]
    assert result.data[0].id == fake_response["data"][0]["id"]
    assert result.links.model_dump() == fake_response["links"]
    assert result.meta.model_dump() == {"errors": None, "total_items": len(fake_response["data"])}
    assert result.data[0].attributes.seller_type == fake_response["data"][0]["attributes"]["seller_type"]
    assert (
        result.data[0].attributes.fee_breakdown.model_dump() == fake_response["data"][0]["attributes"]["fee_breakdown"]
    )
    assert isinstance(result.data[0].attributes.updated_at, datetime)
    assert result.data[0].model_dump() == fake_response["data"][0]


@pytest.mark.parametrize(
    (
        "include_keywords",
        "exclude_keywords",
        "collapse_by_parent",
        "page_size",
        "product_filter_options",
        "seller_types",
        "product_tiers",
        "product_sort_option",
        "fake_response",
    ),
    [
        (
            ["yoga", "gym"],
            ["bath"],
            True,
            5,
            ProductFilterOptions(min_price=100),
            [SellerTypes.AMZ.value],
            [ProductTiers.STANDARD.value],
            ProductSort.NAME.value,
            generate_product_database_responses(total_items=4),
        ),
    ],
)
@respx.mock
@pytest.mark.asyncio()
async def test_collapse_by_parent_request_product_database(
    client_async,
    include_keywords,
    exclude_keywords,
    collapse_by_parent,
    page_size,
    product_filter_options,
    seller_types,
    product_tiers,
    product_sort_option,
    fake_response,
):
    mock_url = f"{client_async.session.base_url}/product_database_query"
    mock_route = respx.post(mock_url).mock(return_value=httpx.Response(200, json=fake_response))
    result = await client_async.product_database(
        include_keywords=include_keywords,
        exclude_keywords=exclude_keywords,
        collapse_by_parent=collapse_by_parent,
        page_size=page_size,
        product_filter_options=product_filter_options,
        seller_types=seller_types,
        product_tiers=product_tiers,
        product_sort_option=product_sort_option,
    )

    assert mock_route.called
    assert mock_route.call_count == 1

    request: httpx.Request = mock_route.calls[0].request
    assert str(request.url.copy_with(query=None)) == mock_url
    assert (
        str(request.url.params) == "marketplace=us&page%5Bsize%5D=5&product_sort_option=-name&collapse_by_parent=true"
    )
    assert request.method == "POST"

    request_content = json.loads(request.content)
    assert request_content == {
        "data": {
            "type": "product_database_query",
            "attributes": {
                "include_keywords": include_keywords,
                "exclude_keywords": exclude_keywords,
                "categories": Marketplace.US.categories,
                "product_tiers": [ProductTiers.STANDARD.value],
                "seller_types": [SellerTypes.AMZ.value],
                "min_price": 100,
            },
        }
    }

    assert len(result.data) == len(fake_response["data"])
    assert isinstance(result, APIResponse)
    assert isinstance(result.data[0], ProductDatabase)
    assert result.data[0].type == fake_response["data"][0]["type"]
    assert result.data[0].id == fake_response["data"][0]["id"]
    assert result.links.model_dump() == fake_response["links"]
    assert result.meta.model_dump() == {"errors": None, "total_items": len(fake_response["data"])}
    assert result.data[0].attributes.seller_type == fake_response["data"][0]["attributes"]["seller_type"]
    assert (
        result.data[0].attributes.fee_breakdown.model_dump() == fake_response["data"][0]["attributes"]["fee_breakdown"]
    )
    assert isinstance(result.data[0].attributes.updated_at, datetime)
    assert result.data[0].model_dump() == fake_response["data"][0]
