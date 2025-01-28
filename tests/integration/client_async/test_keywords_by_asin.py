import pytest
from junglescout import ClientAsync
from junglescout.models.parameters import FilterOptions, Marketplace, Sort


@pytest.mark.integration
@pytest.mark.asyncio
async def test_two_keywords_by_asin(api_keys):
    filter_options = FilterOptions(min_monthly_search_volume_exact=150)
    client = ClientAsync(**api_keys, marketplace=Marketplace.US)
    response = await client.keywords_by_asin(
        asin=["B005IHSKYS", "B0CL5KNB9M"],
        filter_options=filter_options,
        sort_option=Sort.MONTHLY_SEARCH_VOLUME_EXACT_MATCH,
    )
    await client.close()
    assert client.is_closed
    assert response.data is not None


@pytest.mark.integration
@pytest.mark.asyncio
async def test_two_keywords_by_asin_using_context_manager(api_keys):
    filter_options = FilterOptions(min_monthly_search_volume_exact=150)
    async with ClientAsync(**api_keys, marketplace=Marketplace.US) as client:
        response = await client.keywords_by_asin(
            asin=["B005IHSKYS", "B0CL5KNB9M"],
            filter_options=filter_options,
            sort_option=Sort.MONTHLY_SEARCH_VOLUME_EXACT_MATCH,
        )
    assert client.is_closed
    assert response.data is not None


@pytest.mark.integration
@pytest.mark.asyncio
async def test_single_asin_with_sparse_data(api_keys):
    client = ClientAsync(**api_keys, marketplace=Marketplace.US)
    filter_options = FilterOptions(min_monthly_search_volume_exact=150)
    response = await client.keywords_by_asin(
        asin="B005IHSKYS", filter_options=filter_options, sort_option=Sort.MONTHLY_SEARCH_VOLUME_EXACT_MATCH
    )
    await client.close()
    assert client.is_closed
    assert response.data is not None
