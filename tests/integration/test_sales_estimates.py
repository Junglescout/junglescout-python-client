import pytest

from junglescout.client import Client
from junglescout.models.parameters import Marketplace


@pytest.mark.integration()
def test_sales_estimates(api_keys):
    client = Client(**api_keys, marketplace=Marketplace.US)
    response = client.sales_estimates(asin="B078DZ9BRD", start_date="2023-01-01", end_date="2023-12-01")
    assert len(response.data) > 1


@pytest.mark.integration()
def test_sales_estimates_asin_without_rank_data(api_keys):
    client = Client(**api_keys, marketplace=Marketplace.US)
    response = client.sales_estimates(asin="B0CRMZ9PFR", start_date="2023-01-01", end_date="2023-12-01")
    assert response.data == []
    assert response.meta.errors[0].code == "MISSING_RANK_DATA"
