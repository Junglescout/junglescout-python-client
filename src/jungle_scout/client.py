import json
from typing import Optional, NoReturn

from jungle_scout.marketplace import Marketplace
from jungle_scout.session import Session


class Client:
    def __init__(self, api_key_name: str, api_key: str, marketplace: Optional[Marketplace] = None):
        self.session = Session()
        self._marketplace = marketplace
        self._login(api_key_name, api_key)

    def keywords_by_asin(self, asin: str, marketplace: Optional[Marketplace] = None):
        url = self.session.build_url(
            "keywords",
            "keywords_by_asin_query",
            params={
                "marketplace": self._resolve_marketplace(marketplace).value,
                "page[size]": 100,
            },
        )
        payload = json.dumps(
            {
                "data": {
                    "type": "keywords_by_asin_query",
                    "attributes": {"asins": [asin], "include_variants": True, "include_variants_rank": True},
                }
            }
        )
        # TODO: move logic to session??
        response = self.session.request("POST", url, data=payload)
        if response.ok:
            # TODO: translate to model
            return response.json()
        else:
            self._raise_for_status(response)

    def _login(self, api_key_name: str, api_key: str):
        # TODO: implement the `basic_auth` method
        self.session.basic_auth(api_key_name, api_key)

    def _resolve_marketplace(self, provided_marketplace: Optional[Marketplace] = None) -> Marketplace:
        resolved_marketplace = provided_marketplace or self._marketplace
        if isinstance(resolved_marketplace, Marketplace):
            return resolved_marketplace
        else:
            raise AttributeError("Marketplace cannot be resolved")

    @staticmethod
    def _raise_for_status(response: requests.Response) -> NoReturn:
        """
        Method the explicitly raises an exception so type checking tools inference works correctly.
        """
        http_error_message = "Something went wrong"
        try:
            response.raise_for_status()
        except requests.HTTPError as requests_exception:
            http_error_message = requests_exception.args[0]
        raise requests.HTTPError(http_error_message, response=response)
