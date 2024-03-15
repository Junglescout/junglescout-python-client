import json
from abc import ABC, abstractmethod
from typing import Dict, List, Union


# TODO: Update to pydantic model
class BaseResponse(ABC):
    """Base class for response objects."""

    def __init__(self, json_data):
        """Initialize the BaseResponse.

        Args:
            json_data: The raw JSON data received from the API.
        """
        self._json_data = json_data
        self.data = self._update_attributes(json_data)

    @abstractmethod
    def _update_attributes(self, json_data: Dict) -> Union[List[dict], dict]:
        pass

    def as_dict(self):
        """Return the response data as a dictionary."""
        return self._json_data

    def to_json(self):
        """Return the response data as a JSON string."""
        return json.dumps(self.as_dict())
