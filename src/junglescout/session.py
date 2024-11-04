import urllib.parse
from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, TypeVar

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
        self._client = None

    @property
    def client(self) -> T:
        """Returns the client for the session, creating it if necessary."""
        if self._client is None:
            self._client = self._create_client()
        return self._client

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

    @abstractmethod
    def _create_client(self) -> T:
        """Abstract method to create a client. Must be implemented by subclasses."""
        raise NotImplementedError


class SyncSession(Session[httpx.Client]):
    """Represents a synchronous session with the Jungle Scout API."""

    def __init__(self, headers: dict):
        """Initializes a synchronous session with the given headers.

        Args:
            headers: A dictionary of HTTP headers to include in requests.
        """
        super().__init__(headers)

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

    def _create_client(self):
        """Creates and returns a synchronous HTTP client."""
        return httpx.Client(
            headers=self.headers,
            timeout=httpx.Timeout(self.default_timeout_seconds),
        )


class AsyncSession(Session[httpx.AsyncClient]):
    """Represents an asynchronous session with the Jungle Scout API."""

    def __init__(self, headers: dict):
        """Initializes an asynchronous session with the given headers.

        Args:
            headers: A dictionary of HTTP headers to include in requests.
        """
        super().__init__(headers)

    async def request(self, method: str, url: str, **kwargs) -> httpx.Response:
        """Sends a request using the asynchronous client.

        Args:
            method: The HTTP method to use (e.g., 'GET', 'POST').
            url: The URL to send the request to.
            **kwargs: Additional arguments to pass to the request.

        Returns:
            httpx.Response: The response from the server.
        """
        async with self.client as client:
            return await client.request(method, url, **kwargs)

    def _create_client(self):
        """Creates and returns an asynchronous HTTP client."""
        return httpx.AsyncClient(
            headers=self.headers,
            timeout=httpx.Timeout(self.default_timeout_seconds),
        )
