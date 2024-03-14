from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, TypeVar

from jungle_scout.models.parameters import Attributes, Params
from jungle_scout.models.requests.method import Method
from jungle_scout.models.requests.request_type import RequestType

ParamsType = TypeVar("ParamsType", bound=Params)
AttributesType = TypeVar("AttributesType", bound=Attributes)


# TODO: Split request in post and get requests


class BaseRequest(ABC, Generic[ParamsType, AttributesType]):
    """
    Base class for all requests made to the Jungle Scout API.

    Args:
        params (ParamsType): The parameters required for the request.
        attributes (AttributesType): The attributes required for the request.

    Attributes:
        params (Dict): The built parameters for the request.
        payload (Optional[str]): The built payload for the request.

    """

    @property
    @abstractmethod
    def type(self) -> RequestType:
        """
        Get the type of the request.

        Returns:
            RequestType: The type of the request.

        """
        pass

    @property
    @abstractmethod
    def method(self) -> Method:
        """
        Get the HTTP method of the request.

        Returns:
            Method: The HTTP method of the request.

        """
        pass

    def __init__(self, params: ParamsType, attributes: AttributesType):
        """
        Initialize the BaseRequest.

        Args:
            params (ParamsType): The parameters required for the request.
            attributes (AttributesType): The attributes required for the request.

        """
        self.params = self.build_params(params)
        self.payload = self.build_payload(attributes)

    @abstractmethod
    def build_params(self, params: ParamsType) -> Dict:
        """
        Build the parameters for the request.

        Args:
            params (ParamsType): The parameters required for the request.

        Returns:
            Dict: The built parameters for the request.

        """
        pass

    @abstractmethod
    def build_payload(self, attributes: AttributesType) -> Optional[str]:
        """
        Build the payload for the request.

        Args:
            attributes (AttributesType): The attributes required for the request.

        Returns:
            Optional[str]: The built payload for the request.

        """
        pass
