import re
from datetime import datetime
from typing import Dict

from pydantic import field_validator

from jungle_scout.models.parameters import Attributes, Params
from jungle_scout.models.requests import Method, RequestType
from jungle_scout.models.requests.base_request import BaseRequest


class SalesEstimatesParams(Params):
    """
    Represents the parameters for requesting sales estimates.

    Attributes:
        asin (str): The ASIN (Amazon Standard Identification Number) of the product.
        start_date (str): The start date of the sales estimate period in the format YYYY-MM-DD.
        end_date (str): The end date of the sales estimate period in the format YYYY-MM-DD.
    """

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
        assert len(date) == 10, "Date must be in the format YYYY-MM-DD"
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in the format YYYY-MM-DD")
        return date

    # TODO: refactor an re-enable this validation
    # @field_validator("end_date")
    # @classmethod
    # def check_dates(cls, v, values, **kwargs):
    #     if "start_date" in values and v < values["start_date"]:
    #         raise ValueError("end_date must be after start_date")
    #     return v


class SalesEstimatesAttributes(Attributes):
    pass


class SalesEstimatesRequest(BaseRequest[SalesEstimatesParams, SalesEstimatesAttributes]):
    @property
    def type(self) -> RequestType:
        return RequestType.SALES_ESTIMATES

    @property
    def method(self) -> Method:
        return Method.GET

    def build_params(self, params: SalesEstimatesParams) -> Dict:
        return params.model_dump(by_alias=True, exclude_none=True)

    def build_payload(self, attributes: SalesEstimatesAttributes) -> None:
        return None
