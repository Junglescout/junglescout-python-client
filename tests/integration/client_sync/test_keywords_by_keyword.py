import json

import pytest
from pydantic import ValidationError

from junglescout import ClientSync
from junglescout.models.parameters import Marketplace, Sort


@pytest.mark.integration
def test_search_by_keyword_and_category(api_keys):
    search_term = "yoga"
    client = ClientSync(**api_keys, marketplace=Marketplace.US)
    response = client.keywords_by_keyword(
        search_terms=search_term,
        categories=["Home & Kitchen", "Musical Instruments"],
        marketplace=Marketplace.US,
        sort_option=Sort.MONTHLY_TREND,
    )
    client.close()
    assert client.is_closed
    assert response.meta.errors is None
    assert response.meta.total_items is not None
    assert response.meta.total_items > 1
    assert response.links.self is not None
    assert "keywords_by_keyword_query" in response.links.self
    assert response.links.next is None
    assert len(response.data) > 1
    assert response.data[0].id == f"us/{search_term}"
    assert response.data[0].type == "keywords_by_keyword_result"
    assert response.data[0].attributes.country == "us"


@pytest.mark.integration
def test_search_by_keyword_and_category_using_context_manager(api_keys):
    search_term = "yoga"
    with ClientSync(**api_keys, marketplace=Marketplace.US) as client:
        response = client.keywords_by_keyword(
            search_terms=search_term,
            categories=["Home & Kitchen", "Musical Instruments"],
            marketplace=Marketplace.US,
            sort_option=Sort.MONTHLY_TREND,
        )
    assert client.is_closed
    assert response.meta.errors is None
    assert response.meta.total_items is not None
    assert response.meta.total_items > 1
    assert response.links.self is not None
    assert "keywords_by_keyword_query" in response.links.self
    assert response.links.next is None
    assert len(response.data) > 1
    assert response.data[0].id == f"us/{search_term}"
    assert response.data[0].type == "keywords_by_keyword_result"
    assert response.data[0].attributes.country == "us"


@pytest.mark.integration
def test_for_categories_that_do_not_exist(api_keys):
    search_term = "yoga"
    non_existent_category = "This does not exist"
    client = ClientSync(**api_keys, marketplace=Marketplace.US)
    with pytest.raises(ValidationError) as exc_info:
        client.keywords_by_keyword(
            search_terms=search_term,
            categories=[non_existent_category],
            marketplace=Marketplace.US,
            sort_option=Sort.MONTHLY_TREND,
        )
    client.close()

    error_dict = json.loads(exc_info.value.json())[0]
    partial_expected_error_dict = {
        "type": "assertion_error",
        "loc": ["categories"],
        "msg": f"Assertion failed, Category '{non_existent_category}' not found in marketplace categories",
        "input": [non_existent_category],
        "ctx": {"error": f"Category '{non_existent_category}' not found in marketplace categories"},
    }
    assert partial_expected_error_dict.items() <= error_dict.items()
    assert client.is_closed


@pytest.mark.integration
def test_search_by_keyword(api_keys):
    search_term = "Protein Shake"
    client = ClientSync(**api_keys, marketplace=Marketplace.US)
    response = client.keywords_by_keyword(search_terms=search_term)
    client.close()
    assert client.is_closed
    assert response.meta.errors is None
    assert response.meta.total_items is not None
    assert response.meta.total_items > 1
    assert response.links.self is not None
    assert "keywords_by_keyword_query" in response.links.self
    assert len(response.data) > 1
    assert response.data[0].id == f"us/{search_term}"
    assert response.data[0].type == "keywords_by_keyword_result"
    assert response.data[0].attributes.country == "us"
    assert response.data[0].attributes.name == search_term
