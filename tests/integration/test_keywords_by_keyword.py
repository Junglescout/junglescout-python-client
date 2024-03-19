import pytest

from junglescout.client import Client
from junglescout.models.parameters import Marketplace, Sort


@pytest.mark.integration()
def test_keywords_by_keyword(api_keys):
    client = Client(**api_keys, marketplace=Marketplace.US)
    response = client.keywords_by_keyword(
        search_terms="yoga",
        categories=["Home & Kitchen", "Musical Instruments"],
        marketplace=Marketplace.US,
        sort_option=Sort.MONTHLY_TREND,
    )
    assert response.data is not None
