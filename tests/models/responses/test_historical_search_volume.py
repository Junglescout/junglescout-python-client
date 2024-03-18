import json
from datetime import datetime

from jungle_scout.models.responses.historical_search_volume import HistoricalSearchVolume


def test_historical_search_volume():
    response_obj = HistoricalSearchVolume.model_validate_json(
        json.dumps(
            {
                "id": "123",
                "type": "foo",
                "attributes": {
                    "estimate_start_date": datetime(year=2024, month=10, day=5).strftime("%Y-%m-%d"),
                    "estimate_end_date": datetime(year=2024, month=11, day=5).strftime("%Y-%m-%d"),
                    "estimated_exact_search_volume": 5,
                },
            }
        )
    )
    assert isinstance(response_obj, HistoricalSearchVolume)
    assert isinstance(response_obj.attributes.estimate_start_date, datetime)
    assert isinstance(response_obj.attributes.estimate_end_date, datetime)
