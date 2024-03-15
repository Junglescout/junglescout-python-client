import os
from datetime import datetime

import pytest
import requests_mock

from jungle_scout.client import Client
from jungle_scout.models.parameters import (
    Marketplace,
    ProductFilterOptions,
    ProductSort,
    ProductTiers,
    SellerTypes,
)
from jungle_scout.models.responses.product_database import ProductDatabase
from tests.factories.product_database_factory import generate_product_database_responses


@pytest.fixture
def client():
    return Client(api_key_name=os.environ["API_KEY_NAME"], api_key=os.environ["API_KEY"], marketplace=Marketplace.US)


@pytest.mark.parametrize(
    "include_keywords, exclude_keywords, fake_response",
    [
        (["yoga", "gym"], ["bath"], generate_product_database_responses(total_items=1)),
        (["yoga_mat", "mat", "yoga accessories"], ["floor mat"], generate_product_database_responses(total_items=10)),
    ],
)
def test_product_database(client, include_keywords, exclude_keywords, fake_response):
    with requests_mock.Mocker() as mock:
        mock_url = f"{client.session.base_url}/product_database_query"
        mock.post(
            mock_url,
            json=fake_response,
        )

        result = client.product_database(include_keywords=include_keywords, exclude_keywords=exclude_keywords)

    assert mock.called
    assert mock.call_count == 1

    history = mock.request_history

    assert len(history) == 1
    assert history[0].url == f"{mock_url}?marketplace=us&page%5Bsize%5D=10"
    assert history[0].query == "marketplace=us&page%5bsize%5d=10"
    assert history[0].method == "POST"
    assert history[0].json() == {
        "data": {
            "type": "product_database_query",
            "attributes": {
                "include_keywords": include_keywords,
                "exclude_keywords": exclude_keywords,
                "categories": Marketplace.US.categories,
                "product_tiers": [ProductTiers.OVERSIZE.value, ProductTiers.STANDARD.value],
                "seller_types": [SellerTypes.AMZ.value, SellerTypes.FBA.value, SellerTypes.FBM.value],
            },
        }
    }

    assert len(result.data) == len(fake_response["data"])
    assert isinstance(result, ProductDatabase)
    assert result.data[0]["type"] == fake_response["data"][0]["type"]
    assert result.data[0]["id"] == fake_response["data"][0]["id"]
    assert result.links == fake_response["links"]
    assert result.meta == fake_response["meta"]
    assert result.data[0]["attributes"]["seller_type"] == fake_response["data"][0]["attributes"]["seller_type"]
    assert result.data[0]["attributes"]["fee_breakdown"] == fake_response["data"][0]["attributes"]["fee_breakdown"]
    assert isinstance(result.data[0]["attributes"]["updated_at"], datetime)


@pytest.mark.parametrize(
    (
        "include_keywords, exclude_keywords, "
        "page_size, product_filter_options, "
        "seller_types,product_tiers,product_sort_option, fake_response"
    ),
    [
        (
            ["yoga", "gym"],
            ["bath"],
            5,
            ProductFilterOptions(min_price=100),
            [SellerTypes.AMZ.value],
            [ProductTiers.STANDARD.value],
            ProductSort.NAME.value,
            generate_product_database_responses(total_items=4),
        ),
        # (["yoga_mat", "mat", "yoga accessories"], ["floor mat"], generate_product_database_responses(total_items=4)),
    ],
)
def test_full_request_product_database(
    client,
    include_keywords,
    exclude_keywords,
    page_size,
    product_filter_options,
    seller_types,
    product_tiers,
    product_sort_option,
    fake_response,
):
    with requests_mock.Mocker() as mock:
        mock_url = f"{client.session.base_url}/product_database_query"
        mock.post(
            mock_url,
            json=fake_response,
        )

        result = client.product_database(
            include_keywords=include_keywords,
            exclude_keywords=exclude_keywords,
            page_size=page_size,
            product_filter_options=product_filter_options,
            seller_types=seller_types,
            product_tiers=product_tiers,
            product_sort_option=product_sort_option,
        )

    assert mock.called
    assert mock.call_count == 1

    history = mock.request_history

    assert len(history) == 1
    assert history[0].url == f"{mock_url}?marketplace=us&page%5Bsize%5D=5&product_sort_option=-name"
    assert history[0].query == "marketplace=us&page%5bsize%5d=5&product_sort_option=-name"
    assert history[0].method == "POST"
    assert history[0].json() == {
        "data": {
            "type": "product_database_query",
            "attributes": {
                "include_keywords": include_keywords,
                "exclude_keywords": exclude_keywords,
                "categories": Marketplace.US.categories,
                "product_tiers": [ProductTiers.STANDARD.value],
                "seller_types": [SellerTypes.AMZ.value],
                "min_price": 100,
            },
        }
    }

    assert len(result.data) == len(fake_response["data"])
    assert isinstance(result, ProductDatabase)
    assert result.data[0]["type"] == fake_response["data"][0]["type"]
    assert result.data[0]["id"] == fake_response["data"][0]["id"]
    assert result.links == fake_response["links"]
    assert result.meta == fake_response["meta"]
    assert result.data[0]["attributes"]["seller_type"] == fake_response["data"][0]["attributes"]["seller_type"]
    assert result.data[0]["attributes"]["fee_breakdown"] == fake_response["data"][0]["attributes"]["fee_breakdown"]
    assert isinstance(result.data[0]["attributes"]["updated_at"], datetime)
