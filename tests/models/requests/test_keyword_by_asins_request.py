from pydantic import ValidationError

from jungle_scout.models.parameters import FilterOptions, Marketplace, Sort
from jungle_scout.models.requests.keyword_by_asin_request import (
    KeywordByAsinAttributes,
    KeywordByAsinParams,
)


def test_keyword_by_asin_attributes_with_asin_list():
    attributes = KeywordByAsinAttributes(
        filter_options=FilterOptions(min_monthly_search_volume_exact=150),
        asin=["B005IHSKYS", "B0CL5KNB9M"],
        include_variants=True,
    )
    assert attributes.model_dump() == {
        "min_monthly_search_volume_exact": 150,
        "include_variants": True,
        "asins": ["B005IHSKYS", "B0CL5KNB9M"],
    }


def test_keyword_by_asin_attributes_with_individual_asin():
    attributes = KeywordByAsinAttributes(
        filter_options=FilterOptions(min_monthly_search_volume_exact=150, max_monthly_search_volume_broad=1000),
        asin="B005IHSKYS",
        include_variants=True,
    )
    assert attributes.model_dump() == {
        "min_monthly_search_volume_exact": 150,
        "max_monthly_search_volume_broad": 1000,
        "include_variants": True,
        "asins": ["B005IHSKYS"],
    }


def test_keyword_by_asins_raises_error_with_invalid_asin():
    try:
        KeywordByAsinAttributes(
            filter_options=FilterOptions(min_monthly_search_volume_exact=150),
            asin="B005IH",
            include_variants=True,
        )
    except ValidationError as e:
        error_details = e.errors()[0]
        assert error_details["type"] == "assertion_error"
        assert error_details["loc"] == ("asin",)
        assert error_details["msg"] == "Assertion failed, ASIN must be 10 characters long"
    else:
        assert False, "Expected ValueError"


def test_keyword_by_asins_raises_error_with_long_asin_list():
    try:
        KeywordByAsinAttributes(
            filter_options=FilterOptions(min_monthly_search_volume_exact=150),
            asin=[
                "B0CL5KNB9M",
                "B005IHSKYS",
                "B0CL5KNB9M",
                "B005IHSKYS",
                "B0CL5KNB9M",
                "B005IHSKYS",
                "B0CL5KNB9M",
                "B005IHSKYS",
                "B0CL5KNB9M",
                "B005IHSKYS",
                "B005IHSKYS",
            ],
            include_variants=True,
        )
    except ValidationError as e:
        error_details = e.errors()[0]
        assert error_details["type"] == "assertion_error"
        assert error_details["loc"] == ("asin",)
        assert error_details["msg"] == "Assertion failed, ASIN list cannot exceed 10"
    else:
        assert False, "Expected ValueError"


def test_keyword_by_asin_params():
    params = KeywordByAsinParams(
        page_size=50,
        sort=Sort.NAME,
        marketplace=Marketplace.US,
    )
    assert params.model_dump(by_alias=True, exclude_none=True) == {
        "marketplace": "us",
        "sort": "-name",
        "page[size]": 50,
    }
