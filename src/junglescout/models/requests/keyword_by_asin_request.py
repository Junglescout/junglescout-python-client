from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, computed_field, field_validator, model_serializer

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


class KeywordByAsinRequestArgs(BaseModel):
    asin: Union[str, List[str]]
    include_variants: bool
    filter_options: Optional[FilterOptions]
    sort_option: Optional[Sort]
    marketplace: Marketplace
    page_size: Optional[int]
    page: Optional[str]


class KeywordByAsinParams(Params):
    pass


class KeywordByAsinAttributes(Attributes):
    asin: Union[List[str], str]
    include_variants: bool

    @computed_field
    def asins(self) -> List[str]:
        if isinstance(self.asin, str):
            return [self.asin]
        return self.asin

    @field_validator("asin")
    @classmethod
    def validate_asin(cls, v: Union[List[str], str]) -> Union[List[str], str]:
        if isinstance(v, str):
            cls.__validate_individual_asin(v)
        elif isinstance(v, list):
            max_asin_list_length = 10
            assert len(v) <= max_asin_list_length, "ASIN list cannot exceed 10"
            for asin in v:
                cls.__validate_individual_asin(asin)
        else:
            msg = "ASIN must be a string or a list of strings"
            raise TypeError(msg)
        return v

    @staticmethod
    def __validate_individual_asin(asin: str):
        asin_length = 10
        assert len(asin) == asin_length, "ASIN must be 10 characters long"

    @model_serializer
    def serialize_model(self) -> Dict[str, Any]:
        return {
            "asins": self.asins,
            "include_variants": self.include_variants,
            **({} if self.filter_options is None else self.filter_options.model_dump(exclude_none=True)),
        }


class KeywordByAsinRequest(Request[KeywordByAsinRequestArgs, KeywordByAsinParams, KeywordByAsinAttributes]):
    @property
    def url(self) -> str:
        return self.session.build_url("keywords", "keywords_by_asin_query", params=self.params_serialized)

    @property
    def method(self) -> Method:
        return Method.POST

    def serialize_params(self) -> Dict:
        return self.params.model_dump(by_alias=True, exclude_none=True)

    def serialize_payload(self) -> Dict:
        return {
            "data": {
                "type": "keywords_by_asin_query",
                "attributes": self.attributes.model_dump(by_alias=True, exclude_none=True),
            }
        }

    @classmethod
    def from_args(cls, args: KeywordByAsinRequestArgs, session: Session) -> "KeywordByAsinRequest":
        params = KeywordByAsinParams(
            marketplace=args.marketplace, sort=args.sort_option, page=args.page, page_size=args.page_size
        )
        attributes = KeywordByAsinAttributes(
            filter_options=args.filter_options,
            asin=args.asin,
            include_variants=args.include_variants,
        )
        return cls(params=params, attributes=attributes, session=session)
