import urllib.parse
from abc import ABC, abstractmethod
from typing import Coroutine, Dict, Generic, Optional, TypeVar, Union

import httpx

from junglescout.models.parameters import ApiType

T = TypeVar("T")


class Session(ABC, Generic[T]):
    """Represents a session with the Jungle Scout API."""

    def __init__(self, headers: dict, default_timeout_seconds=60):
        """Initializes a new session with the Jungle Scout API.

        Args:
            headers: A dictionary of HTTP headers to include in requests.
            default_timeout_seconds: The default timeout for requests.
        """
        super().__init__()
        self.base_url = "https://developer.junglescout.com/api"
        self.headers = headers
        self.default_timeout_seconds = default_timeout_seconds

    @property
    @abstractmethod
    def client(self) -> T:
        """The httpx client used to make requests to the Jungle Scout API."""

    @abstractmethod
    def close(self) -> Union[None, Coroutine]:
        """Closes the httpx client associated with the session."""

    def build_url(self, *args, params: Optional[Dict] = None):
        """Support function that builds a URL using the base URL and additional path arguments.

        Args:
            *args: Additional path arguments to be appended to the base URL.
            params (Optional[Dict]): Optional dictionary of query parameters.

        Returns:
            str: The constructed URL.

        """
        parts = [self.base_url]
        parts.extend(args)
        parts = [str(p) for p in parts]
        url = "/".join(parts)
        if params:
            return f"{url}?{urllib.parse.urlencode(params)}"
        return url

    def login(self, api_key_name: str, api_key: str, api_type: ApiType = ApiType.JS):
        """Sets the authorization headers for the session.

        Args:
            api_key_name: The name of the API key.
            api_key: The API key.
            api_type: The type of API to use.
        """
        self.headers.update({"Authorization": f"{api_key_name}:{api_key}", "X_API_Type": api_type.value})


class SyncSession(Session[httpx.Client]):
    """Represents a synchronous session with the Jungle Scout API."""

    def __init__(self, headers: dict):
        """Initializes a synchronous session with the given headers.

        Args:
            headers: A dictionary of HTTP headers to include in requests.
        """
        super().__init__(headers)
        self._client: Optional[httpx.Client] = None

    @property
    def client(self) -> httpx.Client:
        """The synchronous httpx client used to make requests to the Jungle Scout API."""
        if self._client is None:
            self._client = httpx.Client(
                headers=self.headers,
                timeout=httpx.Timeout(self.default_timeout_seconds),
            )
        return self._client

    def request(self, method: str, url: str, **kwargs) -> httpx.Response:
        """Sends a request using the synchronous client.

        Args:
            method: The HTTP method to use (e.g., 'GET', 'POST').
            url: The URL to send the request to.
            **kwargs: Additional arguments to pass to the request.

        Returns:
            httpx.Response: The response from the server.
        """
        return self.client.request(method, url, **kwargs)

    def close(self):
        """Closes the synchronous client session."""
        self.client.close()


class AsyncSession(Session[httpx.AsyncClient]):
    """Represents an asynchronous session with the Jungle Scout API."""

    def __init__(self, headers: dict):
        """Initializes an asynchronous session with the given headers.

        Args:
            headers: A dictionary of HTTP headers to include in requests.
        """
        super().__init__(headers)
        self._client: Optional[httpx.AsyncClient] = None

    @property
    def client(self) -> httpx.AsyncClient:
        """The asynchronous httpx client used to make requests to the Jungle Scout API."""
        if self._client is None:
            self._client = httpx.AsyncClient(
                headers=self.headers,
                timeout=httpx.Timeout(self.default_timeout_seconds),
            )
        return self._client

    async def request(self, method: str, url: str, **kwargs) -> httpx.Response:
        """Sends a request using the asynchronous client.

        Args:
            method: The HTTP method to use (e.g., 'GET', 'POST').
            url: The URL to send the request to.
            **kwargs: Additional arguments to pass to the request.

        Returns:
            httpx.Response: The response from the server.
        """
        return await self.client.request(method, url, **kwargs)

    async def close(self):
        """Closes the asynchronous client session."""
        await self.client.aclose()
