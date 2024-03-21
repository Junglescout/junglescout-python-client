from typing import List, NoReturn, Optional, Union

import requests

from junglescout.models.parameters import (
    ApiType,
    FilterOptions,
    Marketplace,
    ProductFilterOptions,
    ProductSort,
    ProductTiers,
    SellerTypes,
    Sort,
)
from junglescout.models.requests.historical_search_volume_request import (
    HistoricalSearchVolumeAttributes,
    HistoricalSearchVolumeParams,
    HistoricalSearchVolumeRequest,
)
from junglescout.models.requests.keyword_by_asin_request import (
    KeywordByAsinAttributes,
    KeywordByAsinParams,
    KeywordByAsinRequest,
)
from junglescout.models.requests.keywords_by_keyword_request import (
    KeywordsByKeywordAttributes,
    KeywordsByKeywordParams,
    KeywordsByKeywordRequest,
)
from junglescout.models.requests.product_database_request import (
    ProductDatabaseAttributes,
    ProductDatabaseParams,
    ProductDatabaseRequest,
)
from junglescout.models.requests.sales_estimates_request import (
    SalesEstimatesAttributes,
    SalesEstimatesParams,
    SalesEstimatesRequest,
)
from junglescout.models.requests.share_of_voice_request import (
    ShareOfVoiceAttributes,
    ShareOfVoiceParams,
    ShareOfVoiceRequest,
)
from junglescout.models.responses import (
    APIResponse,
    HistoricalSearchVolume,
    KeywordByASIN,
    KeywordByKeyword,
    ProductDatabase,
    SalesEstimates,
    ShareOfVoice,
)
from junglescout.session import Session


class Client:
    """The Jungle Scout API client.

    This class is used to make requests to the Jungle Scout API. It provides methods to retrieve keyword data,
    sales estimates, historical search volume, and share of voice data.
    """

    def __init__(
        self,
        api_key_name: str,
        api_key: str,
        api_type: ApiType = ApiType.JS,
        marketplace: Optional[Marketplace] = None,
    ):
        """Initializes the Jungle Scout API client.

        Args:
            api_key_name: The name of the API key.
            api_key: The API key.
            api_type: The type of the API.
            marketplace: The default marketplace to use for API requests.
        """
        self.session = Session()
        self.session.login(api_key_name=api_key_name, api_key=api_key, api_type=api_type)
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
    ) -> APIResponse[List[KeywordByASIN]]:
        """Get keywords by ASIN.

        Args:
            asin: The ASIN (Amazon Standard Identification Number) of the product. This can be a list of
                ASINs or a single ASIN.
            include_variants: Include variants in the response.
            filter_options: Filter options for the request.
            sort_option: Sort option for the request.
            marketplace: The Amazon marketplace.
            page_size: The number of results to return per page.
            page: The page to return.

        Returns:
            The response from the API.
        """
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
            return APIResponse[List[KeywordByASIN]].model_validate(response.json())
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
    ) -> APIResponse[List[KeywordByKeyword]]:
        """Retrieves keyword data based on the provided search terms.

        Args:
            search_terms: The search terms to retrieve keyword data for.
            categories: A list of category names to filter the results by. Must be valid inside the categories of
                the selected Marketplace.
            filter_options: The filter options to apply to the results.
            sort_option: The sort option to apply to the results.
            marketplace: The marketplace to retrieve keyword data from. If not provided, the marketplace provided
                at the client level will be used.
            page_size: The number of results to retrieve per page.
            page: The page token to retrieve a specific page of results. Used in pagination
        Returns:
            The response from the API.

        Raises:
            Exception: If the request to retrieve keyword data fails.
        """
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
            return APIResponse[List[KeywordByKeyword]].model_validate(response.json())
        self._raise_for_status(response)

    def sales_estimates(
        self,
        asin: str,
        start_date: str,
        end_date: str,
        sort_option: Optional[Sort] = None,
        marketplace: Optional[Marketplace] = None,
    ) -> APIResponse[List[SalesEstimates]]:
        """Retrieves sales estimates for a given ASIN within a specified date range.

        Args:
            asin: The ASIN (Amazon Standard Identification Number) of the product.
            start_date: The start date of the date range in the format 'YYYY-MM-DD'.
            end_date: The end date of the date range in the format 'YYYY-MM-DD'.
            sort_option: The sort option for the sales estimates. Must use the Sort enum.
            marketplace: The marketplace to retrieve sales estimates from. If not provided, the marketplace
                provided at the client level will be used.

        Returns:
            The response from the API.

        Raises:
            Exception: If the API request fails or returns an error response.
        """
        marketplace = self._resolve_marketplace(marketplace)

        params = SalesEstimatesParams(
            marketplace=marketplace, sort=sort_option, asin=asin, start_date=start_date, end_date=end_date
        )

        attributes = SalesEstimatesAttributes()

        sales_estimates_request = SalesEstimatesRequest(params, attributes)

        url = self.session.build_url(sales_estimates_request.type.value, params=sales_estimates_request.params)

        response = self.session.request(sales_estimates_request.method.value, url)

        if response.ok:
            return APIResponse[List[SalesEstimates]].model_validate(response.json())
        self._raise_for_status(response)

    def historical_search_volume(
        self,
        keyword: str,
        start_date: str,
        end_date: str,
        sort_option: Optional[Sort] = None,
        marketplace: Optional[Marketplace] = None,
    ) -> APIResponse[List[HistoricalSearchVolume]]:
        """Retrieves the historical search volume for a given keyword within a specified date range.

        Args:
            keyword: The keyword for which to retrieve the historical search volume.
            start_date: The start date of the date range in the format 'YYYY-MM-DD'.
            end_date: The end date of the date range in the format 'YYYY-MM-DD'.
            sort_option: The sort option for the search volume data. Must use the Sort enum.
            marketplace: The marketplace for which to retrieve the search volume data. If not provided,
                the default marketplace will be used.

        Returns:
            The response from the API.

        Raises:
            Exception: If the request to retrieve the historical search volume fails.
        """
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
            return APIResponse[List[HistoricalSearchVolume]].model_validate(response.json())
        self._raise_for_status(response)

    def share_of_voice(
        self,
        keyword: str,
        marketplace: Optional[Marketplace] = None,
    ) -> APIResponse[ShareOfVoice]:
        """Retrieves the share of voice for a given keyword in the specified marketplace.

        Args:
            keyword: The keyword for which to retrieve the share of voice.
            marketplace: The marketplace in which to retrieve the share of voice.
                If not provided, the default marketplace will be used.

        Returns:
            The response from the API.
        """
        marketplace = self._resolve_marketplace(marketplace)

        params = ShareOfVoiceParams(marketplace=marketplace, keyword=keyword)

        attributes = ShareOfVoiceAttributes()

        share_of_voice_request = ShareOfVoiceRequest(params, attributes)

        url = self.session.build_url(share_of_voice_request.type.value, params=share_of_voice_request.params)

        response = self.session.request(share_of_voice_request.method.value, url)

        if response.ok:
            return APIResponse[ShareOfVoice].model_validate(response.json())
        self._raise_for_status(response)

    def product_database(
        self,
        include_keywords: Optional[List[str]] = None,
        exclude_keywords: Optional[List[str]] = None,
        categories: Optional[List[str]] = None,
        product_tiers: Optional[List[ProductTiers]] = None,
        seller_types: Optional[List[SellerTypes]] = None,
        product_filter_options: Optional[ProductFilterOptions] = None,
        product_sort_option: Optional[ProductSort] = None,
        marketplace: Optional[Marketplace] = None,
        page_size: Optional[int] = 10,
        page: Optional[str] = None,
    ) -> APIResponse[List[ProductDatabase]]:
        """Retrieves product data from the Jungle Scout Product Database.

        Args:
            include_keywords: List of keywords or ASINs to include in the search.
            exclude_keywords: List of keywords or ASINs to exclude from the search.
            categories: List of categories to filter the search by. Must be valid inside the
                categories of the selected Marketplace.
            product_tiers: List of product tiers to filter the search by. Must use the ProductTiers enum.
            seller_types: List of seller types to filter the search by. Must use the SellerTypes enum.
            product_filter_options: Additional product filter options. Must use the ProductFilterOptions class.
            product_sort_option: Sorting option for the search results. Must use the ProductSort enum.
            marketplace: Marketplace to search in. If not provided, the default marketplace will be used.
            page_size: Number of results to retrieve per page. Defaults to 10.
            page: Page token for pagination.

        Returns:
            The response from the API.

        Raises:
            Exception: If the request to the Jungle Scout API fails.
        """
        if product_tiers is None:
            product_tiers = [ProductTiers.OVERSIZE, ProductTiers.STANDARD]

        if seller_types is None:
            seller_types = [SellerTypes.AMZ, SellerTypes.FBA, SellerTypes.FBM]

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
            return APIResponse[List[ProductDatabase]].model_validate(response.json())
        self._raise_for_status(response)

    def _resolve_marketplace(self, provided_marketplace: Optional[Marketplace] = None) -> Marketplace:
        """Resolves the marketplace to be used for the API request.

        Args:
            provided_marketplace (Optional[Marketplace]): The marketplace to be used for the API request.
                If not provided, the default marketplace will be used.

        Returns:
            The resolved marketplace.

        Raises:
            AttributeError: If the resolved marketplace is not an instance of the Marketplace class.
        """
        resolved_marketplace = provided_marketplace or self.marketplace
        if isinstance(resolved_marketplace, Marketplace):
            return resolved_marketplace
        msg = "Marketplace cannot be resolved"
        raise AttributeError(msg)

    # TODO: Improve our errors, displaying the actual API message error
    @staticmethod
    def _raise_for_status(response: requests.Response) -> NoReturn:
        http_error_message = "Something went wrong"
        try:
            response.raise_for_status()
        except requests.HTTPError as requests_exception:
            http_error_message = requests_exception.args[0]
        raise requests.HTTPError(http_error_message, response=response)
