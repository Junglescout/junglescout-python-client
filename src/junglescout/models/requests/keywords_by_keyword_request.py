import json
from typing import Any, Dict, List, Optional

from pydantic import ValidationInfo, field_validator, model_serializer

from junglescout.models.parameters import Attributes, Marketplace, Params
from junglescout.models.requests import Method, RequestType
from junglescout.models.requests.base_request import BaseRequest


class KeywordsByKeywordParams(Params):
    pass


class KeywordsByKeywordAttributes(Attributes):
    marketplace: Marketplace
    search_terms: str
    categories: Optional[List[str]] = None

    @field_validator("categories")
    @classmethod
    def validate_categories(cls, v: Optional[List[str]], info: ValidationInfo) -> Optional[List[str]]:
        marketplace = info.data["marketplace"]
        if v:
            for category in v:
                assert category in marketplace.categories, f"Category '{category}' not found in marketplace categories"
        return v

    @model_serializer
    def serialize_model(self) -> Dict[str, Any]:
        serialized_model = {
            "search_terms": self.search_terms,
            "categories": self.categories or self.marketplace.categories,
        }

        if self.filter_options is not None:
            serialized_model.update(**self.filter_options.model_dump(exclude_none=True))

        return serialized_model


class KeywordsByKeywordRequest(BaseRequest[KeywordsByKeywordParams, KeywordsByKeywordAttributes]):
    @property
    def type(self):
        return RequestType.KEYWORDS_BY_KEYWORD

    @property
    def method(self) -> Method:
        return Method.POST

    def build_params(self, params: KeywordsByKeywordParams) -> Dict:  # noqa: PLR6301
        return params.model_dump(by_alias=True, exclude_none=True)

    def build_payload(self, attributes: KeywordsByKeywordAttributes) -> str:
        return json.dumps(
            {"data": {"type": self.type.value, "attributes": attributes.model_dump(by_alias=True, exclude_none=True)}}
        )
