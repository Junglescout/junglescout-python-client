import json
from typing import Dict
from abc import abstractmethod


class BaseModel:
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
