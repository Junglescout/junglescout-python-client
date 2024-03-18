import re
from datetime import datetime
from typing import Dict

from pydantic import field_validator

from junglescout.models.parameters import Attributes, Params
from junglescout.models.requests import Method, RequestType
from junglescout.models.requests.base_request import BaseRequest


class SalesEstimatesParams(Params):
    asin: str
    start_date: str
    end_date: str

    @field_validator("asin")
    @classmethod
    def validate_asin(cls, v: str) -> str:
        assert bool(re.match(r"^(B[\dA-Z]{9}|\d{9}(X|\d))$", v))
        return v

    @field_validator("start_date")
    @classmethod
    def validate_start_date(cls, v: str) -> str:
        return cls.__validate_date(v)

    @field_validator("end_date")
    @classmethod
    def validate_end_date(cls, v: str) -> str:
        return cls.__validate_date(v)

    @staticmethod
    def __validate_date(date: str) -> str:
        valid_date_length = 10
        assert len(date) == valid_date_length, "Date must be in the format YYYY-MM-DD"
        try:
            datetime.strptime(date, "%Y-%m-%d")  # noqa: DTZ007
        except ValueError as exc:
            msg = "Incorrect data format, should be YYYY-MM-DD"
            raise ValueError(msg) from exc
        return date


class SalesEstimatesAttributes(Attributes):
    pass


class SalesEstimatesRequest(BaseRequest[SalesEstimatesParams, SalesEstimatesAttributes]):
    @property
    def type(self) -> RequestType:
        return RequestType.SALES_ESTIMATES

    @property
    def method(self) -> Method:
        return Method.GET

    def build_params(self, params: SalesEstimatesParams) -> Dict:  # noqa: PLR6301
        return params.model_dump(by_alias=True, exclude_none=True)

    def build_payload(self, attributes: SalesEstimatesAttributes) -> None:  # noqa: PLR6301,ARG002
        return None
