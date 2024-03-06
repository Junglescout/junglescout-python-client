from datetime import datetime
from typing import Dict

from pydantic import field_validator

from jungle_scout.models.parameters import Attributes, Params
from jungle_scout.models.requests import Method, RequestType
from jungle_scout.models.requests.base_request import BaseRequest


class HistoricalSearchVolumeParams(Params):
    keyword: str
    start_date: str
    end_date: str

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

    @field_validator("end_date")
    @classmethod
    def check_dates(cls, v, values, **kwargs):
        if "start_date" in values and v < values["start_date"]:
            raise ValueError("end_date must be after start_date")
        return v


class HistoricalSearchVolumeAttributes(Attributes):
    pass


class HistoricalSearchVolumeRequest(BaseRequest[HistoricalSearchVolumeParams, HistoricalSearchVolumeAttributes]):
    @property
    def type(self) -> RequestType:
        return RequestType.HISTORICAL_SEARCH_VOLUME

    @property
    def method(self) -> Method:
        return Method.GET

    def build_params(self, params: HistoricalSearchVolumeParams) -> Dict:
        return params.model_dump(by_alias=True, exclude_none=True)

    def build_payload(self, attributes: HistoricalSearchVolumeAttributes):
        return None
