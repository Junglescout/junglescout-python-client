import json
from typing import List, NoReturn, Optional, Union

import requests
import tenacity

from jungle_scout.models.keyword_by_asin import KeywordByASIN
from jungle_scout.models.keyword_by_keyword import KeywordByKeyword
from jungle_scout.models.parameters.api_type import ApiType
from jungle_scout.models.parameters.marketplace import Marketplace
from jungle_scout.models.parameters.sort import Sort
from jungle_scout.models.parameters.filter_options import FilterOptions
from jungle_scout.session import Session
from jungle_scout.models.requests.keyword_by_asin_request import KeywordByAsinRequest, KeywordByAsinParams, KeywordByAsinAttributes


class Client:
    def __init__(
        self,
        api_key_name: str,
        api_key: str,
        api_type: Optional[ApiType] = ApiType.JS,
        marketplace: Optional[Marketplace] = None,
    ):
        self.session = Session()
        self.session.login(api_key_name=api_key_name, api_key=api_key)
        self.marketplace = marketplace

    @tenacity.retry(
        wait=tenacity.wait_fixed(1),  # Wait 1 second between retries
        stop=tenacity.stop_after_attempt(3),  # Retry 3 times
        retry=tenacity.retry_if_exception_type(
            requests.exceptions.RequestException),  # Retry on RequestException
    )
    def keywords_by_asin(self, asin: Union[str, List[str]], include_variants: bool = True, filterOptions: Optional[FilterOptions] = None, sortOption: Optional[Sort] = None, marketplace: Optional[Marketplace] = None) -> List[KeywordByASIN]:

        keyword_by_asin_request = KeywordByAsinRequest(asin=asin, params=KeywordByAsinParams(
            marketplace=self._resolve_marketplace(marketplace).country_code, sort=sortOption.value), attributes=KeywordByAsinAttributes(
            asins=asin, filter_options=filterOptions, include_variants=include_variants))

        url = self.session.build_url(
            "keywords",
            "keywords_by_asin_query",
            params=keyword_by_asin_request.params
        )

        payload = keyword_by_asin_request.payload

        response = self.session.request("POST", url, data=payload)
        if response.ok:
            return [KeywordByASIN(each) for each in response.json()["data"]]
        else:
            self._raise_for_status(response)

    def keywords_by_keyword(self, search_terms: str, filterOptions: Optional[FilterOptions] = None, marketplace: Optional[Marketplace] = None) -> List[KeywordByKeyword]:
        url = self.session.build_url(
            "keywords",
            "keywords_by_keyword_query",
            params={
                "marketplace": self._resolve_marketplace(marketplace).country_code,
                "sort": Sort.monthly_search_volume_exact.value,
                "page[size]": 50,
            },
        )

        attributes = {"categories": self._resolve_marketplace(marketplace).categories,
                      "search_terms": search_terms}

        if filterOptions is not None:
            attributes.update(vars(filterOptions))

        payload = json.dumps(
            {
                "data": {
                    "type": "keywords_by_keyword_query",
                    "attributes": attributes,
                }
            }
        )

        response = self.session.request("POST", url, data=payload)

        if response.ok:
            return [KeywordByKeyword(each) for each in response.json()["data"]]
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
