from typing import List, NoReturn, Optional, Union

import requests

from jungle_scout.models.parameters import (
    ApiType,
    FilterOptions,
    Marketplace,
    ProductFilterOptions,
    ProductSort,
    ProductTiers,
    SellerTypes,
    Sort,
)
from jungle_scout.models.requests.historical_search_volume_request import (
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
from jungle_scout.models.requests.product_database_request import (
    ProductDatabaseAttributes,
    ProductDatabaseParams,
    ProductDatabaseRequest,
)
from jungle_scout.models.requests.sales_estimates_request import (
    SalesEstimatesAttributes,
    SalesEstimatesParams,
    SalesEstimatesRequest,
)
from jungle_scout.models.requests.share_of_voice_request import (
    ShareOfVoiceAttributes,
    ShareOfVoiceParams,
    ShareOfVoiceRequest,
)
from jungle_scout.models.responses.historical_search_volume import (
    HistoricalSearchVolume,
)
from jungle_scout.models.responses.keyword_by_asin import KeywordByASIN
from jungle_scout.models.responses.keyword_by_keyword import KeywordByKeyword
from jungle_scout.models.responses.product_database import ProductDatabase
from jungle_scout.models.responses.sales_estimates import SalesEstimates
from jungle_scout.models.responses.share_of_voice import ShareOfVoice
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
        page_size: Optional[int] = None,
        page: Optional[str] = None,
    ) -> KeywordByASIN:

        params = KeywordByAsinParams(
            marketplace=self._resolve_marketplace(marketplace), sort=sort_option, page=page, page_size=page_size
        )

        attributes = KeywordByAsinAttributes(
            asin=asin, filter_options=filter_options, include_variants=include_variants
        )

        keyword_by_asin_request = KeywordByAsinRequest(params=params, attributes=attributes)

        url = self.session.build_url(
            "keywords", keyword_by_asin_request.type.value, params=keyword_by_asin_request.params
        )

        payload = keyword_by_asin_request.payload

        response = self.session.request(keyword_by_asin_request.method.value, url, data=payload)
        if response.ok:
            return KeywordByASIN(response.json())
        else:
            self._raise_for_status(response)

    def keywords_by_keyword(
        self,
        search_terms: str,
        categories: Optional[List[str]] = None,
        filter_options: Optional[FilterOptions] = None,
        sort_option: Optional[Sort] = None,
        marketplace: Optional[Marketplace] = None,
        page_size: Optional[int] = None,
        page: Optional[str] = None,
    ) -> KeywordByKeyword:

        marketplace = self._resolve_marketplace(marketplace)

        params = KeywordsByKeywordParams(marketplace=marketplace, sort=sort_option, page=page, page_size=page_size)

        attributes = KeywordsByKeywordAttributes(
            marketplace=marketplace, search_terms=search_terms, filter_options=filter_options, categories=categories
        )

        keywords_by_keyword_request = KeywordsByKeywordRequest(params, attributes)

        url = self.session.build_url(
            "keywords", keywords_by_keyword_request.type.value, params=keywords_by_keyword_request.params
        )

        payload = keywords_by_keyword_request.payload

        response = self.session.request(keywords_by_keyword_request.method.value, url, data=payload)

        if response.ok:
            return KeywordByKeyword(response.json())
        else:
            self._raise_for_status(response)

    def sales_estimates(
        self,
        asin: str,
        start_date: str,
        end_date: str,
        sort_option: Optional[Sort] = None,
        marketplace: Optional[Marketplace] = None,
    ) -> SalesEstimates:

        marketplace = self._resolve_marketplace(marketplace)

        params = SalesEstimatesParams(
            marketplace=marketplace, sort=sort_option, asin=asin, start_date=start_date, end_date=end_date
        )

        attributes = SalesEstimatesAttributes()

        sales_estimates_request = SalesEstimatesRequest(params, attributes)

        url = self.session.build_url(sales_estimates_request.type.value, params=sales_estimates_request.params)

        response = self.session.request(sales_estimates_request.method.value, url)

        if response.ok:
            return SalesEstimates(response.json())
        else:
            self._raise_for_status(response)

    def historical_search_volume(
        self,
        keyword: str,
        start_date: str,
        end_date: str,
        sort_option: Optional[Sort] = None,
        marketplace: Optional[Marketplace] = None,
    ) -> HistoricalSearchVolume:

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
            return HistoricalSearchVolume(response.json())
        else:
            self._raise_for_status(response)

    def share_of_voice(
        self,
        keyword: str,
        marketplace: Optional[Marketplace] = None,
    ) -> ShareOfVoice:

        marketplace = self._resolve_marketplace(marketplace)

        params = ShareOfVoiceParams(marketplace=marketplace, keyword=keyword)

        attributes = ShareOfVoiceAttributes()

        share_of_voice_request = ShareOfVoiceRequest(params, attributes)

        url = self.session.build_url(share_of_voice_request.type.value, params=share_of_voice_request.params)

        response = self.session.request(share_of_voice_request.method.value, url)

        if response.ok:
            return ShareOfVoice(response.json()["data"])
        else:
            self._raise_for_status(response)

    def product_database(
        self,
        include_keywords: Optional[List[str]] = None,
        exclude_keywords: Optional[List[str]] = None,
        categories: Optional[List[str]] = None,
        product_tiers: Optional[List[ProductTiers]] = [ProductTiers.OVERSIZE, ProductTiers.STANDARD],
        seller_types: Optional[List[SellerTypes]] = [SellerTypes.AMZ, SellerTypes.FBA, SellerTypes.FBM],
        product_filter_options: Optional[ProductFilterOptions] = None,
        filter_options: Optional[FilterOptions] = None,
        product_sort_option: Optional[ProductSort] = None,
        marketplace: Optional[Marketplace] = None,
        page_size: Optional[int] = 10,
        page: Optional[str] = None,
    ) -> ProductDatabase:

        marketplace = self._resolve_marketplace(marketplace)

        params = ProductDatabaseParams(
            marketplace=marketplace,
            product_sort_option=product_sort_option,
            page_size=page_size,
            page=page,
        )

        attributes = ProductDatabaseAttributes(
            marketplace=marketplace,
            include_keywords=include_keywords,
            exclude_keywords=exclude_keywords,
            categories=categories,
            product_tiers=product_tiers,
            seller_types=seller_types,
            product_filter_options=product_filter_options,
        )

        product_database_request = ProductDatabaseRequest(params, attributes)

        url = self.session.build_url(product_database_request.type.value, params=product_database_request.params)

        payload = product_database_request.payload

        response = self.session.request(product_database_request.method.value, url, data=payload)

        if response.ok:
            return ProductDatabase(response.json())
        else:
            self._raise_for_status(response)

    def _resolve_marketplace(self, provided_marketplace: Optional[Marketplace] = None) -> Marketplace:
        resolved_marketplace = provided_marketplace or self.marketplace
        if isinstance(resolved_marketplace, Marketplace):
            return resolved_marketplace
        else:
            raise AttributeError("Marketplace cannot be resolved")

    # TODO: Improve our errors, displaying the actual API message error
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
