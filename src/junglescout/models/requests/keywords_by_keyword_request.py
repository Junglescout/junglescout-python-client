from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ValidationInfo, field_validator, model_serializer

from junglescout.models.parameters import (
    Attributes,
    FilterOptions,
    Marketplace,
    Params,
    Sort,
)
from junglescout.models.requests.method import Method
from junglescout.models.requests.request import Request
from junglescout.session import Session


class KeywordsByKeywordArgs(BaseModel):
    search_terms: str
    categories: Optional[List[str]]
    filter_options: Optional[FilterOptions]
    sort_option: Optional[Sort]
    marketplace: Marketplace
    page_size: Optional[int]
    page: Optional[str]


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


class KeywordsByKeywordRequest(Request[KeywordsByKeywordArgs, KeywordsByKeywordParams, KeywordsByKeywordAttributes]):
    @property
    def url(self) -> str:
        return self.session.build_url("keywords", "keywords_by_keyword_query", params=self.params_serialized)

    @property
    def method(self) -> Method:
        return Method.POST

    def serialize_params(self) -> Dict:
        return self.params.model_dump(by_alias=True, exclude_none=True)

    def serialize_payload(self) -> Dict:
        return {
            "data": {
                "type": "keywords_by_keyword_query",
                "attributes": self.attributes.model_dump(by_alias=True, exclude_none=True),
            }
        }

    @classmethod
    def from_args(cls, args: KeywordsByKeywordArgs, session: Session) -> "KeywordsByKeywordRequest":
        params = KeywordsByKeywordParams(
            marketplace=args.marketplace, sort=args.sort_option, page=args.page, page_size=args.page_size
        )
        attributes = KeywordsByKeywordAttributes(
            filter_options=args.filter_options,
            marketplace=args.marketplace,
            search_terms=args.search_terms,
            categories=args.categories,
        )
        return cls(params=params, attributes=attributes, session=session)
