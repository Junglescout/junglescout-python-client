from datetime import datetime

import pytest
from requests.exceptions import HTTPError

from junglescout.client import Client
from junglescout.models.parameters import Marketplace


@pytest.mark.integration()
def test_historical_search_volume(api_keys):
    keyword = "yoga"
    client = Client(**api_keys, marketplace=Marketplace.US)
    response = client.historical_search_volume(keyword=keyword, start_date="2023-04-01", end_date="2023-04-30")
    assert len(response.data) > 1
    assert f"us/{keyword}" in response.data[0].id
    assert response.data[0].type == "historical_keyword_search_volume"
    assert isinstance(response.data[0].attributes.estimate_start_date, datetime)
    assert isinstance(response.data[0].attributes.estimate_end_date, datetime)
    assert response.data[0].attributes.estimated_exact_search_volume > 0


@pytest.mark.integration()
def test_historical_search_volume_with_too_large_of_range(api_keys):
    keyword = "yoga"
    client = Client(**api_keys, marketplace=Marketplace.US)
    with pytest.raises(HTTPError) as exc_info:
        client.historical_search_volume(keyword=keyword, start_date="2023-01-01", end_date="2024-04-30")
    assert exc_info.value.response.json() == {
        "errors": [
            {
                "title": "Invalid parameter value for: 'start_date'",
                "detail": "start_date - start_date and end_date difference must be less or equal than 366 days",
                "code": "BAD_REQUEST",
                "source": {"parameter": "start_date"},
                "status": "400",
            }
        ]
    }


@pytest.mark.integration()
def test_historical_search_volume_with_keyword_that_does_not_exist(api_keys):
    keyword = "thisisnotarealkeywordthisisnotarealkeywordthisisno"
    client = Client(**api_keys, marketplace=Marketplace.US)
    response = client.historical_search_volume(keyword=keyword, start_date="2023-01-01", end_date="2023-04-30")
    assert response.data == []


@pytest.mark.integration()
def test_historical_search_volume_with_old_data(api_keys):
    keyword = "yoga mat"
    client = Client(**api_keys, marketplace=Marketplace.US)
    response = client.historical_search_volume(keyword=keyword, start_date="1960-01-01", end_date="1960-01-31")
    assert response.data == []
