from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, TypeVar

from junglescout.models.parameters import Attributes, Params
from junglescout.models.requests.method import Method
from junglescout.models.requests.request_type import RequestType

ParamsType = TypeVar("ParamsType", bound=Params)
AttributesType = TypeVar("AttributesType", bound=Attributes)


# TODO: Split request in post and get requests


class BaseRequest(ABC, Generic[ParamsType, AttributesType]):
    """Base class for all requests made to the Jungle Scout API."""

    @property
    @abstractmethod
    def type(self) -> RequestType:
        """Get the type of the request.

        Returns:
            RequestType: The type of the request.
        """

    @property
    @abstractmethod
    def method(self) -> Method:
        """Get the HTTP method of the request.

        Returns:
            Method: The HTTP method of the request.
        """

    def __init__(self, params: ParamsType, attributes: AttributesType):
        """Initialize the BaseRequest.

        Args:
            params: The parameters required for the request.
            attributes: The attributes required for the request.
        """
        self.params = self.build_params(params)
        self.payload = self.build_payload(attributes)

    @abstractmethod
    def build_params(self, params: ParamsType) -> Dict:
        """Build the parameters for the request.

        Args:
            params: The parameters required for the request.

        Returns:
            Dict: The built parameters for the request.
        """

    @abstractmethod
    def build_payload(self, attributes: AttributesType) -> Optional[str]:
        """Build the payload for the request.

        Args:
            attributes: The attributes required for the request.

        Returns:
            Optional[str]: The built payload for the request.
        """
