import json
from abc import ABC, abstractmethod
from typing import Dict


class BaseRequest(ABC):
    def __init__(self, request_type, param):
        self.method = json_data
        self.param = json_data
        self.type = request_type

    @abstractmethod
    def build_params(self, json_data: Dict):
        pass

    def build_attributes(self, json_data: Dict):
        pass

    # def as_dict(self):
    #     return self._json_data
