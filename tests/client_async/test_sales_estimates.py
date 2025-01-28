import httpx
import pytest
import respx
from junglescout.models.responses import APIResponse, SalesEstimates

from tests.factories.sales_estimates_factory import generate_sales_estimates_responses


@pytest.mark.parametrize(
    ("asin", "start_date", "end_date", "fake_response"),
    [
        ("B005IHSKYS", "2023-01-01", "2023-02-01", generate_sales_estimates_responses(total_items=1, data_items=3)),
        ("B0CL5KNB9M", "2022-04-01", "2022-05-01", generate_sales_estimates_responses(total_items=4, data_items=2)),
    ],
)
@respx.mock
@pytest.mark.asyncio()
async def test_historical_search_volume(client_async, asin, start_date, end_date, fake_response):
    mock_url = f"{client_async.session.base_url}/sales_estimates_query"
    mock_route = respx.get(mock_url).mock(return_value=httpx.Response(200, json=fake_response))
    result = await client_async.sales_estimates(asin=asin, start_date=start_date, end_date=end_date)

    assert mock_route.called
    assert mock_route.call_count == 1

    request: httpx.Request = mock_route.calls[0].request
    assert str(request.url.copy_with(query=None)) == mock_url
    assert (
        str(request.url.params)
        == f"marketplace=us&page%5Bsize%5D=50&asin={asin}&start_date={start_date}&end_date={end_date}"
    )
    assert request.method == "GET"

    assert isinstance(result, APIResponse)
    assert isinstance(result.data[0], SalesEstimates)
    assert result.data[0].model_dump() == fake_response["data"][0]
    assert len(result.data[0].attributes.data) == len(fake_response["data"][0]["attributes"]["data"])
