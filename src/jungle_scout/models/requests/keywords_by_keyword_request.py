import json
from typing import Dict, List, Optional, TypedDict, Union

from jungle_scout.base_request import BaseRequest
from jungle_scout.models.parameters.filter_options import FilterOptions
from jungle_scout.models.parameters.marketplace import Marketplace
from jungle_scout.models.parameters.sort import Sort


class KeywordsByKeywordParams(TypedDict):
    marketplace: Marketplace
    sort: Optional[Sort]
    page: Optional[str]
    page_size: int = 50


class KeywordsByKeywordAttributes(TypedDict):
    search_terms: str
    categories: Optional[List[str]]
    filter_options: Optional[FilterOptions]


class KeywordsByKeywordRequest(BaseRequest):
    def __init__(self, params: KeywordsByKeywordParams, attributes: KeywordsByKeywordAttributes):
        self.method = "POST"
        self.type = "keywords_by_keyword_query"
        self.params = self.build_params(params)
        self.payload = self.build_payload(attributes, params.get("marketplace") or Marketplace.US)

    def build_payload(self, attributes: KeywordsByKeywordAttributes, marketplace: Marketplace) -> str:
        attributes_dict = {
            "search_terms": attributes.get("search_terms"),
            "categories": attributes.get("categories") or Marketplace.US.categories,
        }

        if attributes.get("filter_options"):
            attributes_dict.update(vars(attributes.get("filter_options")))

        if attributes.get("categories"):
            self._validate_categories(attributes.get("categories"), marketplace)
            attributes_dict.update({"categories": attributes.get("categories")})

        clean_attributes = {k: v for k, v in attributes_dict.items() if v is not None}

        return json.dumps({"data": {"type": self.type, "attributes": clean_attributes}})

    def build_params(self, params: KeywordsByKeywordParams) -> Dict:
        params_dict = {
            "marketplace": params.get("marketplace").country_code,
            "sort": params.get("sort"),
            "page[size]": params.get("page_size", 50),
            "page[cursor]": params.get("page"),
        }

        clean_params = {k: v for k, v in params_dict.items() if v is not None}

        return clean_params

    def _validate_categories(self, categories: Optional[List[str]], marketplace: Marketplace) -> List[str]:
        # check if the objects in the categories lists are inside the current marketplace categories
        categories = categories or marketplace.categories

        for category in categories:
            if category not in marketplace.categories:
                raise ValueError(f"Category '{category}' not found in marketplace categories")

            return categories
