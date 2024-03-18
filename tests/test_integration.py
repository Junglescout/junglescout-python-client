import os

import pytest

from junglescout.client import Client
from junglescout.models.parameters import (
    FilterOptions,
    Marketplace,
    ProductSort,
    ProductTiers,
    SellerTypes,
    Sort,
)

API_KEY_NAME = os.environ["API_KEY_NAME"]
API_KEY = os.environ["API_KEY"]


@pytest.mark.integration()
def test_integration():

    client = Client(api_key_name=API_KEY_NAME, api_key=API_KEY, marketplace=Marketplace.US)

    filter_options = FilterOptions(min_monthly_search_volume_exact=150)

    client.keywords_by_asin(
        asin=["B005IHSKYS", "B0CL5KNB9M"],
        filter_options=filter_options,
        sort_option=Sort.MONTHLY_SEARCH_VOLUME_EXACT_MATCH,
    )

    client.keywords_by_keyword(
        search_terms="yoga",
        categories=["Home & Kitchen", "Musical Instruments"],
        marketplace=Marketplace.US,
        sort_option=Sort.MONTHLY_TREND,
    )

    client.historical_search_volume(keyword="yoga", start_date="2023-04-01", end_date="2023-12-01")

    client.sales_estimates(asin="B078DZ9BRD", start_date="2023-01-01", end_date="2023-12-01")

    client.share_of_voice(keyword="yoga mat", marketplace=Marketplace.US)

    client.product_database(
        include_keywords=["yoga mat", "yoga"],
        exclude_keywords=["mat"],
        marketplace=Marketplace.US,
        page_size=5,
        seller_types=[SellerTypes.AMZ],
        product_tiers=[ProductTiers.OVERSIZE],
        product_sort_option=ProductSort.NAME,
    )
