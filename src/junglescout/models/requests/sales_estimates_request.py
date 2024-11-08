import re
from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel, field_validator

from junglescout.models.parameters import Attributes, Marketplace, Params, Sort
from junglescout.models.requests.method import Method
from junglescout.models.requests.request import Request
from junglescout.session import Session


class SalesEstimatesArgs(BaseModel):
    asin: str
    start_date: str
    end_date: str
    sort_option: Optional[Sort]
    marketplace: Marketplace


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


class SalesEstimatesRequest(Request[SalesEstimatesArgs, SalesEstimatesParams, SalesEstimatesAttributes]):
    @property
    def url(self) -> str:
        return self.session.build_url("sales_estimates_query", params=self.params_serialized)

    @property
    def method(self) -> Method:
        return Method.GET

    def serialize_params(self) -> Dict:
        return self.params.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_args(cls, args: SalesEstimatesArgs, session: Session) -> "SalesEstimatesRequest":
        params = SalesEstimatesParams(
            marketplace=args.marketplace,
            sort=args.sort_option,
            asin=args.asin,
            start_date=args.start_date,
            end_date=args.end_date,
        )
        attributes = SalesEstimatesAttributes()
        return cls(params=params, attributes=attributes, session=session)
