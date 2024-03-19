import pytest

from junglescout.client import Client
from junglescout.models.parameters import FilterOptions, Sort, Marketplace


@pytest.mark.integration()
def test_keywords_by_asin(api_keys):
    client = Client(**api_keys, marketplace=Marketplace.US)
    filter_options = FilterOptions(min_monthly_search_volume_exact=150)
    response = client.keywords_by_asin(
        asin=["B005IHSKYS", "B0CL5KNB9M"],
        filter_options=filter_options,
        sort_option=Sort.MONTHLY_SEARCH_VOLUME_EXACT_MATCH,
    )
    assert response.data is not None
