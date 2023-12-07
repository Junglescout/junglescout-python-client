import json
from typing import List, NoReturn, Optional

import requests

from jungle_scout.marketplace import Marketplace
from jungle_scout.models.keyword_by_asin import KeywordByASIN
from jungle_scout.session import Session


class Client:
    def __init__(self, api_key_name: str, api_key: str, marketplace: Optional[Marketplace] = None):
        self.session = Session()
        self.session.login(api_key_name=api_key_name, api_key=api_key)
        self.marketplace = marketplace

    def keywords_by_asin(self, asin: str, marketplace: Optional[Marketplace] = None) -> List[KeywordByASIN]:
        # TODO: this is a simple way to demonstrate the concept but is lacking many features including
        #       pagination/iteration, retries, more usable interfaces, etc.
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
        response = self.session.request("POST", url, data=payload)
        if response.ok:
            return [KeywordByASIN(each) for each in response.json()["data"]]
        else:
            self._raise_for_status(response)

    def _resolve_marketplace(self, provided_marketplace: Optional[Marketplace] = None) -> Marketplace:
        resolved_marketplace = provided_marketplace or self.marketplace
        if isinstance(resolved_marketplace, Marketplace):
            return resolved_marketplace
        else:
            raise AttributeError("Marketplace cannot be resolved")

    @staticmethod
    def _raise_for_status(response: requests.Response) -> NoReturn:
        """
        Method the explicitly raises an exception so type checking inference works correctly.
        """
        http_error_message = "Something went wrong"
        try:
            response.raise_for_status()
        except requests.HTTPError as requests_exception:
            http_error_message = requests_exception.args[0]
        raise requests.HTTPError(http_error_message, response=response)
