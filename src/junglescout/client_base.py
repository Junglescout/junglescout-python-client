from typing import Optional, NoReturn
import httpx

from junglescout.models.parameters import ApiType, Marketplace
import urllib.parse


class BaseClient:
    def __init__(
        self,
        api_key_name: str,
        api_key: str,
        api_type: ApiType = ApiType.JS,
        marketplace: Optional[Marketplace] = None,
    ):
        self.api_key_name = api_key_name
        self.api_key = api_key
        self.api_type = api_type
        self.marketplace = marketplace
        self.base_url = "https://developer.junglescout.com/api"

    def _build_headers(self) -> dict:
        return {
            "Accept": "application/vnd.junglescout.v1+json",
            "Content-Type": "application/vnd.api+json",
            #"Authorization": f"{self.api_key_name}:{self.api_key}",
            #"X_API_Type": self.api_type.value,
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
        http_error_message = "Something went wrong"
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as httpx_exception:
            http_error_message = f"{httpx_exception.args[0]} - {response.json()}"
            httpx_exception_request = httpx_exception.request
        raise httpx.HTTPStatusError(http_error_message, request=httpx_exception_request, response=response)