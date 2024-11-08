import json
from types import TracebackType
from typing import List, Optional, Type, Union

from junglescout.client import Client
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
    HistoricalSearchVolumeArgs,
    HistoricalSearchVolumeRequest,
)
from junglescout.models.requests.keyword_by_asin_request import (
    KeywordByAsinRequest,
    KeywordByAsinRequestArgs,
)
from junglescout.models.requests.keywords_by_keyword_request import (
    KeywordsByKeywordArgs,
    KeywordsByKeywordRequest,
)
from junglescout.models.requests.product_database_request import (
    ProductDatabaseArgs,
    ProductDatabaseRequest,
)
from junglescout.models.requests.sales_estimates_request import (
    SalesEstimatesArgs,
    SalesEstimatesRequest,
)
from junglescout.models.requests.share_of_voice_request import (
    ShareOfVoiceArgs,
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
from junglescout.session import SyncSession


class ClientSync(Client[SyncSession]):
    """The Jungle Scout Synchronous API client.

    This class is used to make synchronous requests to the Jungle Scout API.
    """

    def __init__(
        self,
        api_key_name: str,
        api_key: str,
        api_type: ApiType = ApiType.JS,
        marketplace: Optional[Marketplace] = None,
    ):
        """Initializes the Jungle Scout Synchronous API client.

        Args:
            api_key_name: The name of the API key.
            api_key: The API key.
            api_type: The type of the API.
            marketplace: The default marketplace to use for API requests.
        """
        super().__init__(api_key_name, api_key, api_type, marketplace)
        self._session: Optional[SyncSession] = None

    @property
    def session(self) -> SyncSession:
        """The session used to make requests to the Jungle Scout API."""
        if self._session is None:
            headers = self._build_headers()
            self._session = SyncSession(headers)
            self._session.login(api_key_name=self.api_key_name, api_key=self.api_key, api_type=self.api_type)
        return self._session

    def close(self) -> None:
        """Closes all connections used by the client."""
        if self._session is not None:
            self.session.client.close()
            self._session = None

    @property
    def is_closed(self) -> bool:
        """Boolean indicating if the client session is closed."""
        if self._session is not None:
            return self.session.client.is_closed
        return True

    def __enter__(self) -> "ClientSync":
        """Enter the context manager.

        Returns:
            self: The client instance.
        """
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_val: Optional[BaseException] = None,
        exc_tb: Optional[TracebackType] = None,
    ) -> None:
        """Exit the context manager and cleanup resources.

        Args:
            exc_type: The type of the exception that occurred, if any.
            exc_val: The instance of the exception that occurred, if any.
            exc_tb: The traceback of the exception that occurred, if any.
        """
        self.close()

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
        args = KeywordByAsinRequestArgs(
            asin=asin,
            include_variants=include_variants,
            filter_options=filter_options,
            sort_option=sort_option,
            marketplace=self._resolve_marketplace(marketplace),
            page_size=page_size,
            page=page,
        )
        request_instance = KeywordByAsinRequest.from_args(args, self.session)
        response = self.session.request(
            request_instance.method.value, request_instance.url, json=request_instance.payload_serialized
        )
        if response.is_success:
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
        args = KeywordsByKeywordArgs(
            search_terms=search_terms,
            categories=categories,
            filter_options=filter_options,
            sort_option=sort_option,
            marketplace=self._resolve_marketplace(marketplace),
            page_size=page_size,
            page=page,
        )
        request_instance = KeywordsByKeywordRequest.from_args(args, self.session)
        response = self.session.request(
            request_instance.method.value,
            request_instance.url,
            content=json.dumps(request_instance.payload_serialized).encode("utf-8"),
        )
        if response.is_success:
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
        args = SalesEstimatesArgs(
            asin=asin,
            start_date=start_date,
            end_date=end_date,
            sort_option=sort_option,
            marketplace=self._resolve_marketplace(marketplace),
        )
        request_instance = SalesEstimatesRequest.from_args(args, self.session)
        response = self.session.request(request_instance.method.value, request_instance.url)
        if response.is_success:
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
        args = HistoricalSearchVolumeArgs(
            keyword=keyword,
            start_date=start_date,
            end_date=end_date,
            sort_option=sort_option,
            marketplace=self._resolve_marketplace(marketplace),
        )
        request_instance = HistoricalSearchVolumeRequest.from_args(args, self.session)
        response = self.session.request(request_instance.method.value, request_instance.url)
        if response.is_success:
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
        args = ShareOfVoiceArgs(
            keyword=keyword,
            marketplace=self._resolve_marketplace(marketplace),
        )
        request_instance = ShareOfVoiceRequest.from_args(args, self.session)
        response = self.session.request(request_instance.method.value, request_instance.url)
        if response.is_success:
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
        args = ProductDatabaseArgs(
            include_keywords=include_keywords,
            exclude_keywords=exclude_keywords,
            categories=categories,
            product_tiers=product_tiers,
            seller_types=seller_types,
            product_filter_options=product_filter_options,
            product_sort_option=product_sort_option,
            marketplace=self._resolve_marketplace(marketplace),
            page_size=page_size,
            page=page,
        )
        request_instance = ProductDatabaseRequest.from_args(args, self.session)
        response = self.session.request(
            request_instance.method.value,
            request_instance.url,
            content=json.dumps(request_instance.payload_serialized).encode("utf-8"),
        )
        if response.is_success:
            return APIResponse[List[ProductDatabase]].model_validate(response.json())
        self._raise_for_status(response)
