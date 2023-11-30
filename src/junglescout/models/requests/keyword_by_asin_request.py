import json
from typing import Any, Dict, List, Union

from pydantic import computed_field, field_validator, model_serializer

from junglescout.models.parameters import Attributes, Params
from junglescout.models.requests import Method, RequestType
from junglescout.models.requests.base_request import BaseRequest


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


class KeywordByAsinRequest(BaseRequest[KeywordByAsinParams, KeywordByAsinAttributes]):
    @property
    def type(self):
        return RequestType.KEYWORDS_BY_ASIN

    @property
    def method(self) -> Method:
        return Method.POST

    def build_params(self, params: KeywordByAsinParams) -> Dict:  # noqa: PLR6301
        return params.model_dump(by_alias=True, exclude_none=True)

    def build_payload(self, attributes: KeywordByAsinAttributes) -> str:
        return json.dumps(
            {"data": {"type": self.type.value, "attributes": attributes.model_dump(by_alias=True, exclude_none=True)}}
        )
