from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, Type, TypeVar

from junglescout.models.parameters import Attributes, Params
from junglescout.models.requests.method import Method
from junglescout.session import Session

ArgsType = TypeVar("ArgsType")
ParamsType = TypeVar("ParamsType", bound=Params)
AttributesType = TypeVar("AttributesType", bound=Attributes)


class Request(ABC, Generic[ArgsType, ParamsType, AttributesType]):
    """Base class for all requests made to the Jungle Scout API."""

    def __init__(self, params: ParamsType, attributes: AttributesType, session: Session):
        """Initialize the BaseRequest.

        Args:
            params: The parameters required for the request.
            attributes: The attributes required for the request.
            session: The session to use for the request.
        """
        self.params: ParamsType = params
        self.attributes: AttributesType = attributes
        self.session: Session = session
        self.params_serialized = self.serialize_params()
        self.payload_serialized = self.serialize_payload()

    @property
    @abstractmethod
    def url(self) -> str:
        """Get the URL for the request.

        Returns:
            The URL for the request.
        """

    @property
    @abstractmethod
    def method(self) -> Method:
        """Get the HTTP method of the request.

        Returns:
            The HTTP method of the request.
        """

    @abstractmethod
    def serialize_params(self) -> Dict:
        """Serialize the parameters for the request.

        Returns:
            The built parameters for the request.
        """

    def serialize_payload(self) -> Optional[Dict]:  # noqa: PLR6301
        """Serialize the payload for the request.

        Returns:
            The payload for the request.
        """
        return None

    @classmethod
    @abstractmethod
    def from_args(
        cls: Type["Request[ArgsType, ParamsType, AttributesType]"], args: ArgsType, session: Session
    ) -> "Request[ArgsType, ParamsType, AttributesType]":
        """Factory method to create a request from arguments.

        Args:
            args: The arguments to create the request from.
            session: The session to use for the request.

        Returns:
            The created request.
        """
