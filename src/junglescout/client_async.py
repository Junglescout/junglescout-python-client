from typing import List, Optional, Union

from junglescout.client import Client
from junglescout.models.parameters import ApiType, FilterOptions, Marketplace, Sort
from junglescout.models.requests.keyword_by_asin_request import (
    KeywordByAsinRequest,
    KeywordByAsinRequestArgs,
)
from junglescout.models.responses import APIResponse, KeywordByASIN
from junglescout.session import AsyncSession


class ClientAsync(Client[AsyncSession]):
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
        super().__init__(api_key_name, api_key, api_type, marketplace)

    def create_session(self) -> AsyncSession:
        """Creates a new AsyncSession."""
        headers = self._build_headers()
        return AsyncSession(headers)

    async def keywords_by_asin(
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
            sort_option: Sort option for the request. This is equivalent to -sort_option in the API.
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
        response = await self.session.request(
            request_instance.method.value, request_instance.url, json=request_instance.payload_serialized
        )
        if response.is_success:
            return APIResponse[List[KeywordByASIN]].model_validate(response.json())
        self._raise_for_status(response)
