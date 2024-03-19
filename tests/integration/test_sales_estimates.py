import pytest

from junglescout.client import Client
from junglescout.models.parameters import Marketplace


@pytest.mark.integration()
def test_sales_estimates(api_keys):
    client = Client(**api_keys, marketplace=Marketplace.US)
    response = client.sales_estimates(asin="B078DZ9BRD", start_date="2023-01-01", end_date="2023-12-01")
    assert response.data is not None
