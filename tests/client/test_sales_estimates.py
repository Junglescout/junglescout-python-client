import os

import pytest
import requests_mock

from jungle_scout.client import Client
from jungle_scout.models.parameters import Marketplace
from tests.factories.sales_estimates_factory import generate_sales_estimates_responses


@pytest.fixture()
def client():
    return Client(api_key_name=os.environ["API_KEY_NAME"], api_key=os.environ["API_KEY"], marketplace=Marketplace.US)


@pytest.mark.parametrize(
    ("asin", "start_date", "end_date", "fake_response"),
    [
        ("B005IHSKYS", "2023-01-01", "2023-02-01", generate_sales_estimates_responses(total_items=1, data_items=3)),
        ("B0CL5KNB9M", "2022-04-01", "2022-05-01", generate_sales_estimates_responses(total_items=4, data_items=2)),
    ],
)
def test_historical_search_volume(client, asin, start_date, end_date, fake_response):
    with requests_mock.Mocker() as mock:
        mock_url = f"{client.session.base_url}/sales_estimates_query"
        mock.get(
            mock_url,
            json=fake_response,
        )

        result = client.sales_estimates(asin=asin, start_date=start_date, end_date=end_date)

    assert mock.called
    assert mock.call_count == 1

    history = mock.request_history
    assert len(history) == 1
    assert (
        history[0].url
        == f"{mock_url}?marketplace=us&page%5Bsize%5D=50&asin={asin}&start_date={start_date}&end_date={end_date}"
    )
    assert (
        history[0].query
        == f"marketplace=us&page%5bsize%5d=50&asin={asin.lower()}&start_date={start_date}&end_date={end_date}"
    )
    assert history[0].method == "GET"

    assert result.data[0] == fake_response["data"][0]
    assert len(result.data[0]["attributes"]["data"]) == len(fake_response["data"][0]["attributes"]["data"])
