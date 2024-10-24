import httpx


class JungleScoutError(Exception):
    """Base exception for all Jungle Scout Exceptions."""


class JungleScoutHTTPError(JungleScoutError):
    """Base exception for Jungle Scout HTTP errors."""

    def __init__(
        self,
        message: str,
        httpx_exception: httpx.HTTPError,
    ):
        """Initializes a new Jungle Scout HTTP error.

        Args:
            message: The error message.
            httpx_exception: The underlying HTTPX exception.
        """
        super().__init__(message)
        self.httpx_exception = httpx_exception
