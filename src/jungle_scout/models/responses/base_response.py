import json
from abc import ABC, abstractmethod
from typing import Dict


# TODO: Update to pydantic model
class BaseResponse(ABC):
    def __init__(self, json_data):
        self._json_data = json_data
        self._update_attributes(json_data)

    @abstractmethod
    def _update_attributes(self, json_data: Dict):
        pass

    def as_dict(self):
        return self._json_data

    def to_json(self):
        return json.dumps(self.as_dict())
