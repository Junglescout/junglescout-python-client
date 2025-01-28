from datetime import datetime

import pytest

from junglescout import ClientAsync
from junglescout.models.parameters import (
    Marketplace,
    ProductSort,
    ProductTiers,
    SellerTypes,
)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_with_keywords(api_keys):
    client = ClientAsync(**api_keys, marketplace=Marketplace.US)
    response = await client.product_database(
        include_keywords=["yoga mat", "yoga"],
        exclude_keywords=["mat"],
        marketplace=Marketplace.US,
        page_size=5,
        seller_types=[SellerTypes.AMZ],
        product_tiers=[ProductTiers.OVERSIZE],
        product_sort_option=ProductSort.NAME,
    )
    await client.close()
    assert client.is_closed
    assert response.data is not None
    assert response.meta.errors is None
    assert response.meta.total_items is not None
    assert response.meta.total_items > 1
    assert response.links.next is not None
    assert "product_database_query" in response.links.next
    assert len(response.data) > 1
    assert response.data[0].id.startswith("us")
    assert response.data[0].type == "product_database_result"
    assert isinstance(response.data[0].attributes.updated_at, datetime)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_with_keywords_using_context_manager(api_keys):
    async with ClientAsync(**api_keys, marketplace=Marketplace.US) as client:
        response = await client.product_database(
            include_keywords=["yoga mat", "yoga"],
            exclude_keywords=["mat"],
            marketplace=Marketplace.US,
            page_size=5,
            seller_types=[SellerTypes.AMZ],
            product_tiers=[ProductTiers.OVERSIZE],
            product_sort_option=ProductSort.NAME,
        )
    assert client.is_closed
    assert response.data is not None
    assert response.meta.errors is None
    assert response.meta.total_items is not None
    assert response.meta.total_items > 1
    assert response.links.next is not None
    assert "product_database_query" in response.links.next
    assert len(response.data) > 1
    assert response.data[0].id.startswith("us")
    assert response.data[0].type == "product_database_result"
    assert isinstance(response.data[0].attributes.updated_at, datetime)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_with_only_keywords(api_keys):
    client = ClientAsync(**api_keys, marketplace=Marketplace.US)
    response = await client.product_database(
        include_keywords=["yoga mat", "yoga"],
        marketplace=Marketplace.DE,
        page_size=5,
        product_sort_option=ProductSort.NAME,
    )
    await client.close()
    assert client.is_closed
    assert response.data is not None
    assert response.meta.errors is None
    assert response.meta.total_items is not None
    assert response.meta.total_items > 1
    assert response.links.next is not None
    assert "product_database_query" in response.links.next
    assert len(response.data) > 1
    assert response.data[0].id.startswith("de")
    assert response.data[0].type == "product_database_result"
    assert isinstance(response.data[0].attributes.updated_at, datetime)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_with_keyword_that_does_not_exist(api_keys):
    keywords = ["thisisnotarealkeywordthisisnotarealkeywordthisisno"]
    client = ClientAsync(**api_keys, marketplace=Marketplace.US)
    response = await client.product_database(
        include_keywords=keywords,
        marketplace=Marketplace.US,
    )
    await client.close()
    assert client.is_closed
    assert response.data == []
    assert response.links.next is None
