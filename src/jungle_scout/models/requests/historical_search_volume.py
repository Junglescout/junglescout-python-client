import json
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import ValidationInfo, field_validator, model_serializer

from jungle_scout.base_request import BaseRequest
from jungle_scout.models.parameters.attributes import Attributes
from jungle_scout.models.parameters.marketplace import Marketplace
from jungle_scout.models.parameters.params import Params
from jungle_scout.models.requests.method import Method
from jungle_scout.models.requests.request_type import RequestType


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


class HistoricalSearchVolumeAttributes(Attributes):
    pass


class HistoricalSearchVolumeRequest(BaseRequest[HistoricalSearchVolumeParams, HistoricalSearchVolumeAttributes]):
    type: RequestType = RequestType.HISTORICAL_SEARCH_VOLUME
    method: Method = Method.GET

    def build_params(self, params: HistoricalSearchVolumeParams) -> Dict:
        return params.model_dump(by_alias=True, exclude_none=True)

    def build_payload(self, attributes: HistoricalSearchVolumeAttributes) -> str:
        pass
