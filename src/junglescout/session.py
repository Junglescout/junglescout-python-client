import urllib.parse
from typing import Dict, Optional

import requests

from junglescout.models.parameters import ApiType


class Session(requests.Session):
    """Represents a session with the Jungle Scout API."""

    def __init__(self, default_connect_timeout=4, default_read_timeout=10):
        """Initializes a new session with the Jungle Scout API.

        Args:
            default_connect_timeout: The default connection timeout in seconds.
            default_read_timeout: The default read timeout in seconds.
        """
        super().__init__()
        self.default_connect_timeout = default_connect_timeout
        self.default_read_timeout = default_read_timeout
        self.headers.update(
            {
                "Accept": "application/vnd.junglescout.v1+json",
                "Content-Type": "application/vnd.api+json",
            }
        )
        self.base_url = "https://developer.junglescout.com/api"

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
            api_key: The API
            api_type: The type of API to use.
        """
        self.headers.update({"Authorization": f"{api_key_name}:{api_key}", "X_API_Type": api_type.value})
