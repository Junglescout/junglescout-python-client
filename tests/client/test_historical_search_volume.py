import os

import pytest
import requests_mock

from jungle_scout.client import Client
from jungle_scout.models.parameters import Marketplace, Sort
from tests.factories.historical_search_volume_factory import (
    generate_historical_search_volume_responses,
)


@pytest.fixture()
def client():
    return Client(api_key_name=os.environ["API_KEY_NAME"], api_key=os.environ["API_KEY"], marketplace=Marketplace.US)


@pytest.mark.parametrize(
    "keyword, start_date, end_date, fake_response",
    [
        ("yoga", "2023-01-01", "2023-02-01", generate_historical_search_volume_responses(total_items=5)),
        ("ps5", "2022-04-01", "2022-05-01", generate_historical_search_volume_responses(total_items=10)),
    ],
)
#  mock a GET request to the historical_search_volume endpoint


def test_historical_search_volume(client, keyword, start_date, end_date, fake_response):
    with requests_mock.Mocker() as mock:
        mock_url = f"{client.session.base_url}/keywords/historical_search_volume"
        mock.get(
            mock_url,
            json=fake_response,
        )

        result = client.historical_search_volume(keyword=keyword, start_date=start_date, end_date=end_date)

    assert mock.called
    assert mock.call_count == 1

    history = mock.request_history
    assert len(history) == 1
    assert (
        history[0].url
        == f"{mock_url}?marketplace=us&page%5Bsize%5D=50&keyword={keyword}&start_date={start_date}&end_date={end_date}"
    )
    assert (
        history[0].query
        == f"marketplace=us&page%5bsize%5d=50&keyword={keyword}&start_date={start_date}&end_date={end_date}"
    )
    assert history[0].method == "GET"

    assert result.data[0] == fake_response["data"][0]


@pytest.mark.parametrize(
    "keyword, start_date, end_date, sort_options, marketplace, fake_response",
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
#  mock a GET request to the historical_search_volume endpoint


def test_historical_search_volume_sort_options(
    client, keyword, start_date, end_date, sort_options, marketplace, fake_response
):
    with requests_mock.Mocker() as mock:
        mock_url = f"{client.session.base_url}/keywords/historical_search_volume"
        mock.get(
            mock_url,
            json=fake_response,
        )

        result = client.historical_search_volume(
            keyword=keyword, start_date=start_date, end_date=end_date, sort_option=sort_options, marketplace=marketplace
        )

    assert mock.called
    assert mock.call_count == 1

    history = mock.request_history
    assert len(history) == 1
    assert history[0].url == (
        f"{mock_url}?marketplace={marketplace.country_code}&"
        f"sort={sort_options.value}&page%5Bsize%5D=50&"
        f"keyword={keyword}&start_date={start_date}&end_date={end_date}"
    )
    assert history[0].query == (
        f"marketplace={marketplace.country_code}&"
        f"sort={sort_options.value}&page%5bsize%5d=50&"
        f"keyword={keyword}&start_date={start_date}&end_date={end_date}"
    )
    assert history[0].method == "GET"

    assert result.data[0] == fake_response["data"][0]
