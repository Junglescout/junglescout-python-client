import pytest

from junglescout.client import Client
from junglescout.models.parameters import Marketplace, SellerTypes, ProductTiers, ProductSort


@pytest.mark.integration()
def test_product_database(api_keys):
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
