from typing import Dict

from pydantic import BaseModel

from junglescout.models.parameters import Attributes, Marketplace, Params
from junglescout.models.requests import Method, RequestType
from junglescout.models.requests.request import Request
from junglescout.session import Session


class ShareOfVoiceArgs(BaseModel):
    keyword: str
    marketplace: Marketplace


class ShareOfVoiceParams(Params):
    keyword: str


class ShareOfVoiceAttributes(Attributes):
    pass


class ShareOfVoiceRequest(Request[ShareOfVoiceArgs, ShareOfVoiceParams, ShareOfVoiceAttributes]):
    @property
    def url(self) -> str:
        return self.session.build_url(self.type.value, params=self.params_serialized)

    @property
    def type(self) -> RequestType:
        return RequestType.SHARE_OF_VOICE

    @property
    def method(self) -> Method:
        return Method.GET

    def serialize_params(self) -> Dict:
        return self.params.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_args(cls, args: ShareOfVoiceArgs, session: Session) -> "ShareOfVoiceRequest":
        params = ShareOfVoiceParams(
            marketplace=args.marketplace,
            keyword=args.keyword,
        )
        attributes = ShareOfVoiceAttributes()
        return cls(params=params, attributes=attributes, session=session)
