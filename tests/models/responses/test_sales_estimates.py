import json
from datetime import datetime

from jungle_scout.models.responses.sales_estimates import SalesEstimates


def test_sales_estimates():
    response_obj = SalesEstimates.model_validate_json(
        json.dumps(
            {
                "id": "123",
                "type": "foo",
                "attributes": {
                    "asin": "foo",
                    "is_parent": True,
                    "is_variant": True,
                    "is_standalone": True,
                    "parent_asin": "foo",
                    "variants": 1,
                    "data": [
                        {
                            "date": "2024-11-05",
                            "estimated_units_sold": 5,
                            "last_known_price": 5.0,
                        },
                        {
                            "date": "2024-11-05",
                            "estimated_units_sold": 5,
                            "last_known_price": 5.0,
                        },
                    ],
                },
            }
        )
    )
    assert isinstance(response_obj, SalesEstimates)
    count_of_data_objects = 2
    assert len(response_obj.attributes.data) == count_of_data_objects
    assert isinstance(response_obj.attributes.data[0].date, datetime)
