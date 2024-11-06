import pytest
from httpx import HTTPStatusError

from junglescout import Client
from junglescout.exceptions import JungleScoutHTTPError
from junglescout.models.parameters import Marketplace

HTTP_UNPROCESSABLE_ENTITY_CODE = 422


@pytest.mark.integration()
def test_sales_estimates(api_keys):
    variant_asin = "B078DZ9BRD"
    client = Client(**api_keys, marketplace=Marketplace.US)
    response = client.sales_estimates(asin=variant_asin, start_date="2023-01-01", end_date="2023-01-31")
    assert len(response.data) == 1
    assert response.data[0].id == f"us/{variant_asin}"
    assert response.data[0].type == "sales_estimate_result"
    assert response.data[0].attributes.asin == variant_asin
    assert response.data[0].attributes.is_parent is False
    assert response.data[0].attributes.is_variant is True
    assert response.data[0].attributes.is_standalone is False
    assert response.data[0].attributes.variants == []
    assert len(response.data[0].attributes.data) > 1


@pytest.mark.integration()
@pytest.mark.skip("This test is skipped because the ASIN currently has rank data.")
def test_sales_estimates_asin_without_rank_data(api_keys):
    client = Client(**api_keys, marketplace=Marketplace.US)
    with pytest.raises(JungleScoutHTTPError) as exc_info:
        client.sales_estimates(asin="B0CRMZ9PFR", start_date="2023-01-01", end_date="2023-12-01")
    assert isinstance(exc_info.value.httpx_exception, HTTPStatusError)
    assert exc_info.value.httpx_exception.response.status_code == HTTP_UNPROCESSABLE_ENTITY_CODE
    assert exc_info.value.httpx_exception.response.json()["errors"][0]["code"] == "MISSING_RANK_DATA"


@pytest.mark.integration()
def test_sales_estimates_asin_with_variants(api_keys):
    parent_asin = "B0CQHGPJS2"
    client = Client(**api_keys, marketplace=Marketplace.US)
    response = client.sales_estimates(asin=parent_asin, start_date="2024-01-01", end_date="2024-01-31")
    assert len(response.data) == 1
    assert response.data[0].attributes.asin == parent_asin
    assert response.data[0].attributes.is_parent is True
    assert response.data[0].attributes.is_variant is False
    assert response.data[0].attributes.is_standalone is False
    assert response.data[0].attributes.parent_asin == parent_asin
