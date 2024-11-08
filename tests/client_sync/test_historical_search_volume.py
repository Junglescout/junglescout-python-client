import httpx
import pytest
import respx

from junglescout.models.parameters import Marketplace, Sort
from tests.factories.historical_search_volume_factory import (
    generate_historical_search_volume_responses,
)


@pytest.mark.parametrize(
    ("keyword", "start_date", "end_date", "fake_response"),
    [
        ("yoga", "2023-01-01", "2023-02-01", generate_historical_search_volume_responses(total_items=5)),
        ("ps5", "2022-04-01", "2022-05-01", generate_historical_search_volume_responses(total_items=10)),
    ],
)
@respx.mock
def test_historical_search_volume(client_sync, keyword, start_date, end_date, fake_response):
    mock_url = f"{client_sync.session.base_url}/keywords/historical_search_volume"
    mock_route = respx.get(mock_url).mock(return_value=httpx.Response(200, json=fake_response))
    result = client_sync.historical_search_volume(keyword=keyword, start_date=start_date, end_date=end_date)

    assert mock_route.called
    assert mock_route.call_count == 1

    request: httpx.Request = mock_route.calls[0].request
    assert str(request.url.copy_with(query=None)) == mock_url
    assert (
        str(request.url.params)
        == f"marketplace=us&page%5Bsize%5D=50&keyword={keyword}&start_date={start_date}&end_date={end_date}"
    )
    assert request.method == "GET"
    assert result.data[0].model_dump() == fake_response["data"][0]


@pytest.mark.parametrize(
    ("keyword", "start_date", "end_date", "sort_options", "marketplace", "fake_response"),
    [
        (
            "yoga",
            "2023-01-01",
            "2023-02-01",
            Sort.MONTHLY_SEARCH_VOLUME_EXACT_MATCH,
            Marketplace.US,
            generate_historical_search_volume_responses(total_items=5),
        ),
        (
            "ps5",
            "2022-12-01",
            "2023-03-01",
            Sort.MONTHLY_TREND,
            Marketplace.CA,
            generate_historical_search_volume_responses(total_items=10),
        ),
    ],
)
@respx.mock
def test_historical_search_volume_sort_options(
    client_sync, keyword, start_date, end_date, sort_options, marketplace, fake_response
):
    mock_url = f"{client_sync.session.base_url}/keywords/historical_search_volume"
    mock_route = respx.get(mock_url).mock(return_value=httpx.Response(200, json=fake_response))
    result = client_sync.historical_search_volume(
        keyword=keyword, start_date=start_date, end_date=end_date, sort_option=sort_options, marketplace=marketplace
    )

    assert mock_route.called
    assert mock_route.call_count == 1

    request: httpx.Request = mock_route.calls[0].request
    assert str(request.url.copy_with(query=None)) == mock_url
    assert str(request.url.params) == (
        f"marketplace={marketplace.country_code}&"
        f"sort={sort_options.value}&page%5Bsize%5D=50&"
        f"keyword={keyword}&start_date={start_date}&end_date={end_date}"
    )
    assert request.method == "GET"

    assert result.data[0].model_dump() == fake_response["data"][0]
