from typing import Dict

from junglescout.models.parameters import Attributes, Params
from junglescout.models.requests import Method, RequestType
from junglescout.models.requests.base_request import BaseRequest


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

    def build_params(self, params: ShareOfVoiceParams) -> Dict:  # noqa: PLR6301
        return params.model_dump(by_alias=True, exclude_none=True)

    def build_payload(self, attributes: ShareOfVoiceAttributes):  # noqa: PLR6301,ARG002
        return None
