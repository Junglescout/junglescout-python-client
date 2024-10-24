import urllib.parse
from abc import ABC, abstractmethod
from typing import Generic, NoReturn, Optional, TypeVar

import httpx

from junglescout.exceptions import JungleScoutError, JungleScoutHTTPError
from junglescout.models.parameters import ApiType, Marketplace
from junglescout.session import BaseSession

T = TypeVar("T", bound=BaseSession)


class Client(ABC, Generic[T]):
    """Base class for Jungle Scout API clients."""

    def __init__(
        self,
        api_key_name: str,
        api_key: str,
        api_type: ApiType = ApiType.JS,
        marketplace: Optional[Marketplace] = None,
    ):
        """Initializes a new Jungle Scout API client.

        Args:
            api_key_name: The name of the API key.
            api_key: The API key.
            api_type: The type of API to use.
            marketplace: The default marketplace to use for API requests.
        """
        self.api_key_name = api_key_name
        self.api_key = api_key
        self.api_type = api_type
        self.marketplace = marketplace
        self.base_url = "https://developer.junglescout.com/api"
        self.session: T = self.create_session()
        self.session.login(api_key_name=api_key_name, api_key=api_key, api_type=api_type)

    @abstractmethod
    def create_session(self) -> T:
        """Abstract method to create a session. Must be implemented by subclasses."""
        raise NotImplementedError

    @staticmethod
    def _build_headers() -> dict:
        return {
            "Accept": "application/vnd.junglescout.v1+json",
            "Content-Type": "application/vnd.api+json",
        }

    def _build_url(self, *args, params: Optional[dict] = None) -> str:
        url = "/".join([self.base_url, *map(str, args)])
        if params:
            url += f"?{urllib.parse.urlencode(params)}"
        return url

    def _resolve_marketplace(self, provided_marketplace: Optional[Marketplace] = None) -> Marketplace:
        resolved_marketplace = provided_marketplace or self.marketplace
        if isinstance(resolved_marketplace, Marketplace):
            return resolved_marketplace
        msg = "Marketplace cannot be resolved"
        raise AttributeError(msg)

    # TODO: Improve our errors, displaying the actual API message error
    @staticmethod
    def _raise_for_status(response: httpx.Response) -> NoReturn:
        uncaught_exception = Exception
        default_error_message = "Something went wrong"
        try:
            response.raise_for_status()
        except httpx.HTTPError as http_error_exc:
            try:
                error_message = f"{http_error_exc.args[0]} - {response.json()}"
            except ValueError:
                error_message = default_error_message
            raise JungleScoutHTTPError(error_message, http_error_exc) from http_error_exc
        except Exception as exc:
            uncaught_exception = exc
        raise JungleScoutError(default_error_message) from uncaught_exception
