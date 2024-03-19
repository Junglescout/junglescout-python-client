import pytest

from junglescout.client import Client
from junglescout.models.parameters import Marketplace


@pytest.mark.integration()
def test_historical_search_volume(api_keys):
    client = Client(**api_keys, marketplace=Marketplace.US)
    response = client.historical_search_volume(keyword="yoga", start_date="2023-04-01", end_date="2023-12-01")
    assert response.data is not None
