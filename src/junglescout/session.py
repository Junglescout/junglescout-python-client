import urllib.parse
from typing import Dict, Optional

import httpx

from junglescout.models.parameters import ApiType


class BaseSession():
    """Represents a session with the Jungle Scout API."""

    def __init__(self, headers: Optional[dict] = None, default_connect_timeout=4, default_read_timeout=10):
        """Initializes a new session with the Jungle Scout API.

        Args:
            default_connect_timeout: The default connection timeout in seconds.
            default_read_timeout: The default read timeout in seconds.
        """
        super().__init__()
        self.default_connect_timeout = default_connect_timeout
        self.default_read_timeout = default_read_timeout
        self.base_url = "https://developer.junglescout.com/api"
        self.headers = headers
        self.client = None

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


class SyncSession(BaseSession):
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

    def login(self, api_key_name: str, api_key: str, api_type: ApiType = ApiType.JS):
        """Sets the authorization headers for the session.

        Args:
            api_key_name: The name of the API key.
            api_key: The API key.
            api_type: The type of API to use.
        """
        super().login(api_key_name, api_key, api_type)
        self.client = httpx.Client(
            headers=self.headers,
            timeout=httpx.Timeout(
                timeout=self.default_read_timeout,
                connect=self.default_connect_timeout,
                read=self.default_read_timeout,
            ),
        )


class AsyncSession(BaseSession):
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
            request = await self.client.request(method, url, **kwargs)
        return request

    def login(self, api_key_name: str, api_key: str, api_type: ApiType = ApiType.JS):
        super().login(api_key_name, api_key, api_type)
        self.client = httpx.AsyncClient(
            headers=self.headers,
            timeout=httpx.Timeout(
                timeout=self.default_read_timeout,
                connect=self.default_connect_timeout,
                read=self.default_read_timeout,
            ),
        )
