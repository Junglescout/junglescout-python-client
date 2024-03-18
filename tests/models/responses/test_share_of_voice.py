from jungle_scout.models.responses.share_of_voice import ShareOfVoice
from datetime import datetime
import json


def test_share_of_voice():
    response_obj = ShareOfVoice.model_validate_json(
        json.dumps(
            {
                "type": "foo",
                "id": "123",
                "attributes": {
                    "estimated_30_day_search_volume": 1,
                    "exact_suggested_bid_median": 1.0,
                    "product_count": 1,
                    "updated_at": datetime(year=2023, month=10, day=5).strftime("%Y-%m-%d"),
                    "brands": [
                        {
                            "brand": "foo",
                            "combined_products": "foo",
                            "combined_weighted_sov": 1.0,
                            "combined_basic_sov": 1.0,
                            "combined_average_position": 1,
                            "combined_average_price": 1.0,
                            "organic_products": "foo",
                            "organic_weighted_sov": 1,
                            "organic_basic_sov": 1,
                            "organic_average_position": 1,
                            "organic_average_price": 1.0,
                            "sponsored_products": "foo",
                            "sponsored_weighted_sov": 1,
                            "sponsored_basic_sov": 1,
                            "sponsored_average_position": 1,
                            "sponsored_average_price": 1.0,
                        },
                    ],
                    "top_asins": [
                        {
                            "asin": "foo",
                            "name": "foo",
                            "brand": "foo",
                            "clicks": 1,
                            "conversions": 1,
                            "conversion_rate": 1.0,
                        },
                    ],
                    "top_asins_model_start_date": datetime(year=2023, month=10, day=5).strftime("%Y-%m-%d"),
                    "top_asins_model_end_date": datetime(year=2023, month=11, day=5).strftime("%Y-%m-%d"),
                },
            }
        )
    )
    assert isinstance(response_obj, ShareOfVoice)
    assert isinstance(response_obj.attributes.updated_at, datetime)
    assert isinstance(response_obj.attributes.brands[0].combined_average_price, float)
