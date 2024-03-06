import os

import pytest

from jungle_scout.client import Client
from jungle_scout.models.parameters.filter_options import FilterOptions
from jungle_scout.models.parameters.marketplace import Marketplace
from jungle_scout.models.parameters.sort import Sort

API_KEY_NAME = os.environ["API_KEY_NAME"]
API_KEY = os.environ["API_KEY"]


@pytest.mark.skip(reason="Integration tests are run manually for now.")
def test_integration():

    client = Client(api_key_name=API_KEY_NAME, api_key=API_KEY, marketplace=Marketplace.US)

    #  Defines the filter options
    filter_options = FilterOptions(min_monthly_search_volume_exact=150)

    keywords_by_asin = client.keywords_by_asin(
        asin=["B005IHSKYS", "B0CL5KNB9M"], filter_options=filter_options, sort_option=Sort.monthly_search_volume_exact
    )

    keywords_by_keyword = client.keywords_by_keyword(
        search_terms="yoga",
        categories=["Home & Kitchen", "Musical Instruments"],
        marketplace=Marketplace.US,
        sort_option=Sort.monthly_trend,
    )

    for keyword in keywords_by_asin[:10]:
        print(keyword.name)

    print("------")

    for keyword in keywords_by_keyword[:10]:
        print(keyword.name)
