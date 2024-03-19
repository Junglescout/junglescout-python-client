from datetime import datetime

import pytest

from junglescout.client import Client
from junglescout.models.parameters import (
    Marketplace,
    ProductSort,
    ProductTiers,
    SellerTypes,
)


@pytest.mark.integration()
def test_with_keywords(api_keys):
    client = Client(**api_keys, marketplace=Marketplace.US)
    response = client.product_database(
        include_keywords=["yoga mat", "yoga"],
        exclude_keywords=["mat"],
        marketplace=Marketplace.US,
        page_size=5,
        seller_types=[SellerTypes.AMZ],
        product_tiers=[ProductTiers.OVERSIZE],
        product_sort_option=ProductSort.NAME,
    )
    assert response.data is not None
    assert response.meta.errors is None
    assert response.meta.total_items > 1
    assert "product_database_query" in response.links.next
    assert len(response.data) > 1
    assert response.data[0].id.startswith("us")
    assert response.data[0].type == "product_database_result"
    assert isinstance(response.data[0].attributes.updated_at, datetime)


@pytest.mark.integration()
def test_with_keyword_that_does_not_exist(api_keys):
    keywords = ["thisisnotarealkeywordthisisnotarealkeywordthisisno"]
    client = Client(**api_keys, marketplace=Marketplace.US)
    response = client.product_database(
        include_keywords=keywords,
        marketplace=Marketplace.US,
    )
    assert response.data == []
    assert response.meta.total_items == 0
