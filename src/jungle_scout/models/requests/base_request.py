from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, TypeVar

from jungle_scout.models.parameters import Attributes, Params
from jungle_scout.models.requests.method import Method
from jungle_scout.models.requests.request_type import RequestType

ParamsType = TypeVar("ParamsType", bound=Params)
AttributesType = TypeVar("AttributesType", bound=Attributes)


# TODO: Split request in post and get requests
class BaseRequest(ABC, Generic[ParamsType, AttributesType]):
    @property
    @abstractmethod
    def type(self) -> RequestType:
        pass

    @property
    @abstractmethod
    def method(self) -> Method:
        pass

    def __init__(self, params: ParamsType, attributes: AttributesType):
        self.params = self.build_params(params)
        self.payload = self.build_payload(attributes)

    @abstractmethod
    def build_params(self, params: ParamsType) -> Dict:
        pass

    @abstractmethod
    def build_payload(self, attributes: AttributesType) -> Optional[str]:
        pass