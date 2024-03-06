import json
from typing import Any, Dict, List, Optional

from pydantic import field_validator, model_serializer, ValidationInfo

from jungle_scout.base_request import BaseRequest
from jungle_scout.models.parameters.attributes import Attributes
from jungle_scout.models.parameters.marketplace import Marketplace
from jungle_scout.models.parameters.params import Params
from jungle_scout.models.requests.method import Method
from jungle_scout.models.requests.request_type import RequestType


class KeywordsByKeywordParams(Params):
    pass


class KeywordsByKeywordAttributes(Attributes):
    marketplace: Marketplace
    search_terms: str
    categories: Optional[List[str]] = None

    @field_validator("categories")
    @classmethod
    def validate_categories(cls, v: Optional[List[str]], info: ValidationInfo) -> Optional[List[str]]:
        marketplace = info.data['marketplace']
        if v:
            for category in v:
                assert (
                    category in marketplace.categories
                ), f"Category '{category}' not found in marketplace categories"
        return v

    @model_serializer
    def serialize_model(self) -> Dict[str, Any]:
        serialized_model = {
            "search_terms": self.search_terms,
            "categories": self.categories or self.marketplace.categories
        }

        if self.filter_options is not None:
            serialized_model.update(
                **self.filter_options.model_dump(exclude_none=True))

        return serialized_model


class KeywordsByKeywordRequest(BaseRequest[KeywordsByKeywordParams, KeywordsByKeywordAttributes]):
    type: RequestType = RequestType.KEYWORDS_BY_KEYWORD
    method: Method = Method.POST

    def build_params(self, params: KeywordsByKeywordParams) -> Dict:
        return params.model_dump(by_alias=True, exclude_none=True)

    def build_payload(self, attributes: KeywordsByKeywordAttributes) -> str:
        return json.dumps(
            {"data": {"type": self.type.value, "attributes": attributes.model_dump(
                by_alias=True, exclude_none=True)}}
        )
