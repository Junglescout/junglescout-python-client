from typing import Dict

from jungle_scout.models.parameters import Attributes, Params
from jungle_scout.models.requests import Method, RequestType
from jungle_scout.models.requests.base_request import BaseRequest


class ShareOfVoiceParams(Params):
    """Represents the parameters for a Share of Voice request.

    Attributes:
        keyword (str): The keyword for which the Share of Voice data is requested.
    """

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
