import json
from typing import List, NoReturn, Optional, Union

import requests

from jungle_scout.models.keyword_by_asin import KeywordByASIN
from jungle_scout.models.keyword_by_keyword import KeywordByKeyword
from jungle_scout.models.parameters.api_type import ApiType
from jungle_scout.models.parameters.filter_options import FilterOptions
from jungle_scout.models.parameters.marketplace import Marketplace
from jungle_scout.models.parameters.sort import Sort
from jungle_scout.models.requests.historical_search_volume import (
    HistoricalSearchVolumeAttributes,
    HistoricalSearchVolumeParams,
    HistoricalSearchVolumeRequest,
)
from jungle_scout.models.requests.keyword_by_asin_request import (
    KeywordByAsinAttributes,
    KeywordByAsinParams,
    KeywordByAsinRequest,
)
from jungle_scout.models.requests.keywords_by_keyword_request import (
    KeywordsByKeywordAttributes,
    KeywordsByKeywordParams,
    KeywordsByKeywordRequest,
)
from jungle_scout.session import Session


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

    def keywords_by_asin(
        self,
        asin: Union[str, List[str]],
        include_variants: bool = True,
        filter_options: Optional[FilterOptions] = None,
        sort_option: Optional[Sort] = None,
        marketplace: Optional[Marketplace] = None,
    ) -> List[KeywordByASIN]:

        params = KeywordByAsinParams(marketplace=self._resolve_marketplace(marketplace), sort=sort_option)

        attributes = KeywordByAsinAttributes(
            asin=asin, filter_options=filter_options, include_variants=include_variants
        )

        keyword_by_asin_request = KeywordByAsinRequest(params=params, attributes=attributes)

        url = self.session.build_url("keywords", "keywords_by_asin_query", params=keyword_by_asin_request.params)

        payload = keyword_by_asin_request.payload

        response = self.session.request(keyword_by_asin_request.method.value, url, data=payload)
        if response.ok:
            return [KeywordByASIN(each) for each in response.json()["data"]]
        else:
            self._raise_for_status(response)

    def keywords_by_keyword(
        self,
        search_terms: str,
        categories: Optional[List[str]] = None,
        filter_options: Optional[FilterOptions] = None,
        sort_option: Optional[Sort] = None,
        marketplace: Optional[Marketplace] = None,
    ) -> List[KeywordByKeyword]:

        marketplace = self._resolve_marketplace(marketplace)

        params = KeywordsByKeywordParams(marketplace=marketplace, sort=sort_option)

        attributes = KeywordsByKeywordAttributes(
            marketplace=marketplace, search_terms=search_terms, filter_options=filter_options, categories=categories
        )

        keywords_by_keyword_request = KeywordsByKeywordRequest(params, attributes)

        url = self.session.build_url("keywords", "keywords_by_keyword_query", params=keywords_by_keyword_request.params)

        payload = keywords_by_keyword_request.payload

        response = self.session.request(keywords_by_keyword_request.method.value, url, data=payload)

        if response.ok:
            return [KeywordByKeyword(each) for each in response.json()["data"]]
        else:
            self._raise_for_status(response)

    def historical_search_volume(
        self,
        keyword: str,
        start_date: str,
        end_date: str,
        sort_option: Optional[Sort] = None,
        marketplace: Optional[Marketplace] = None,
    ) -> List[KeywordByKeyword]:

        marketplace = self._resolve_marketplace(marketplace)

        params = HistoricalSearchVolumeParams(
            marketplace=marketplace, sort=sort_option, keyword=keyword, start_date=start_date, end_date=end_date
        )

        attributes = HistoricalSearchVolumeAttributes()

        historical_search_volume_request = HistoricalSearchVolumeRequest(params, attributes)

        url = self.session.build_url(
            "keywords", historical_search_volume_request.type.value, params=historical_search_volume_request.params
        )

        response = self.session.request(historical_search_volume_request.method.value, url)

        if response.ok:
            print(response.json()["data"])
            # return [KeywordByKeyword(each) for each in response.json()["data"]]
            return response.json()["data"]
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
