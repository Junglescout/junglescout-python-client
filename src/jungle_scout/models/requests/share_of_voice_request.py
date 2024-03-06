import json
import re
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import ValidationInfo, field_validator, model_serializer, validator

from jungle_scout.base_request import BaseRequest
from jungle_scout.models.parameters.attributes import Attributes
from jungle_scout.models.parameters.marketplace import Marketplace
from jungle_scout.models.parameters.params import Params
from jungle_scout.models.requests.method import Method
from jungle_scout.models.requests.request_type import RequestType


class ShareOfVoiceParams(Params):
    keyword: str


class ShareOfVoiceAttributes(Attributes):
    pass


class ShareOfVoiceRequest(BaseRequest[ShareOfVoiceParams, ShareOfVoiceAttributes]):
    @property
    def type(self) -> RequestType:
        return RequestType.SHARE_OF_VOICE

    @property
    def method(self) -> Method:
        return Method.GET

    def build_params(self, params: ShareOfVoiceParams) -> Dict:
        return params.model_dump(by_alias=True, exclude_none=True)

    def build_payload(self, attributes: ShareOfVoiceAttributes):
        return None
