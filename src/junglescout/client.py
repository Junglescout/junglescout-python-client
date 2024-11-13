import urllib.parse
from abc import ABC, abstractmethod
from typing import Generic, NoReturn, Optional, TypeVar

import httpx

from junglescout import __version__ as package_version
from junglescout.exceptions import JungleScoutError, JungleScoutHTTPError
from junglescout.models.parameters import ApiType, Marketplace
from junglescout.session import Session

T = TypeVar("T", bound=Session)


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

    @property
    @abstractmethod
    def session(self) -> T:
        """The session used to make requests to the Jungle Scout API."""

    @property
    @abstractmethod
    def is_closed(self) -> bool:
        """Boolean indicating if the client session is closed."""

    @staticmethod
    def _build_headers() -> dict:
        return {
            "Accept": "application/vnd.junglescout.v1+json",
            "Content-Type": "application/vnd.api+json",
            "X-Client-Id": f"python-client-{package_version}",
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
        except RuntimeError as exc:
            uncaught_exception = exc
        raise JungleScoutError(default_error_message) from uncaught_exception
