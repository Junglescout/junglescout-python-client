from abc import ABC, abstractmethod
from typing import Dict, TypeVar, Generic

from jungle_scout.models.parameters.attributes import Attributes
from jungle_scout.models.parameters.params import Params
from jungle_scout.models.requests.method import Method

ParamsType = TypeVar("ParamsType", bound=Params)
AttributesType = TypeVar("AttributesType", bound=Attributes)


class BaseRequest(ABC, Generic[ParamsType, AttributesType]):
    def __init__(self, params: ParamsType, attributes: AttributesType):
        self.params = self.build_params(params)
        self.payload = self.build_payload(attributes)

    @property
    @abstractmethod
    def type(self) -> str:
        pass

    @property
    @abstractmethod
    def method(self) -> Method:
        pass

    @abstractmethod
    def build_params(self, params: ParamsType) -> Dict:
        pass

    @abstractmethod
    def build_payload(self, attributes: AttributesType) -> str:
        pass
