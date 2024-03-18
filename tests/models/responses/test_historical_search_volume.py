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
                    "estimate_start_date": "2024-11-05",
                    "estimate_end_date": "2024-12-05",
                    "estimated_exact_search_volume": 5,
                },
            }
        )
    )
    assert isinstance(response_obj, HistoricalSearchVolume)
    assert isinstance(response_obj.attributes.estimate_start_date, datetime)
    assert isinstance(response_obj.attributes.estimate_end_date, datetime)
