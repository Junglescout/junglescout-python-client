import json
from typing import Dict, List, Optional, Any

from pydantic import model_serializer, field_validator

from jungle_scout.base_request import BaseRequest
from jungle_scout.models.parameters.attributes import Attributes
from jungle_scout.models.parameters.marketplace import Marketplace
from jungle_scout.models.parameters.params import Params
from jungle_scout.models.requests.method import Method


class KeywordsByKeywordParams(Params):
    pass


class KeywordsByKeywordAttributes(Attributes):
    marketplace: Marketplace
    search_terms: str
    categories: Optional[List[str]] = None

    @field_validator("categories")
    def validate_categories(cls, v: Optional[List[str]]) -> Optional[List[str]]:
        if v:
            for category in v:
                assert (
                    category in cls.marketplace.categories
                ), f"Category '{category}' not found in marketplace categories"
        return v

    @model_serializer
    def serialize_model(self) -> Dict[str, Any]:
        return {
            "search_terms": self.search_terms,
            "categories": self.categories or self.marketplace.categories,
            **self.filter_options.model_dump(exclude_none=True),
        }


class KeywordsByKeywordRequest(BaseRequest[KeywordsByKeywordParams, KeywordsByKeywordAttributes]):
    @property
    def method(self) -> Method:
        return Method.POST

    @property
    def type(self) -> str:
        return "keywords_by_keyword_query"

    def build_params(self, params: KeywordsByKeywordParams) -> Dict:
        return params.model_dump(by_alias=True, exclude_none=True)

    def build_payload(self, attributes: KeywordsByKeywordAttributes) -> str:
        return json.dumps(
            {"data": {"type": self.type, "attributes": attributes.model_dump(by_alias=True, exclude_none=True)}}
        )
