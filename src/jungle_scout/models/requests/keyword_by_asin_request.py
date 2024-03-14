import json
from typing import Any, Dict, List, Union

from pydantic import computed_field, field_validator, model_serializer

from jungle_scout.models.parameters import Attributes, Params
from jungle_scout.models.requests import Method, RequestType
from jungle_scout.models.requests.base_request import BaseRequest


class KeywordByAsinParams(Params):
    pass


class KeywordByAsinAttributes(Attributes):
    """Represents the attributes for a KeywordByAsin request.

    Attributes:
        asin (Union[List[str], str]): The ASIN(s) to retrieve keywords for. Can be a single ASIN or a list of ASINs.
        include_variants (bool): Flag indicating whether to include variants in the results.
    """

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
            assert len(v) <= 10, "ASIN list cannot exceed 10"
            for asin in v:
                cls.__validate_individual_asin(asin)
        else:
            raise ValueError("asin must be a string or a list of strings")
        return v

    @staticmethod
    def __validate_individual_asin(asin: str):
        assert len(asin) == 10, "ASIN must be 10 characters long"

    @model_serializer
    def serialize_model(self) -> Dict[str, Any]:
        return {
            "asins": self.asins,
            "include_variants": self.include_variants,
            **({} if self.filter_options is None else self.filter_options.model_dump(exclude_none=True)),
        }


class KeywordByAsinRequest(BaseRequest[KeywordByAsinParams, KeywordByAsinAttributes]):
    """Represents a request to retrieve keywords by ASIN.

    Inherits from BaseRequest and specifies the type, method, and payload for the request.

    Args:
        params (KeywordByAsinParams): The parameters for the request.
        attributes (KeywordByAsinAttributes): The attributes for the request.

    Returns:
        str: The JSON payload for the request.

    """

    @property
    def type(self):
        return RequestType.KEYWORDS_BY_ASIN

    @property
    def method(self) -> Method:
        return Method.POST

    def build_params(self, params: KeywordByAsinParams) -> Dict:
        return params.model_dump(by_alias=True, exclude_none=True)

    def build_payload(self, attributes: KeywordByAsinAttributes) -> str:
        return json.dumps(
            {"data": {"type": self.type.value, "attributes": attributes.model_dump(by_alias=True, exclude_none=True)}}
        )
