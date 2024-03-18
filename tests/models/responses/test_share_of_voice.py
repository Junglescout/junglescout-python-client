import json
from datetime import datetime

from jungle_scout.models.responses.share_of_voice import ShareOfVoice


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
                    "updated_at": "2024-11-05",
                    "brands": [
                        {
                            "brand": "foo",
                            "combined_products": 1,
                            "combined_weighted_sov": 1,
                            "combined_basic_sov": 1,
                            "combined_average_position": 1,
                            "combined_average_price": 1.0,
                            "organic_products": 1,
                            "organic_weighted_sov": 1,
                            "organic_basic_sov": 1,
                            "organic_average_position": 1,
                            "organic_average_price": 1.0,
                            "sponsored_products": 1,
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
                    "top_asins_model_start_date": "2024-11-05",
                    "top_asins_model_end_date": "2024-11-05",
                },
            }
        )
    )
    assert isinstance(response_obj, ShareOfVoice)
    assert isinstance(response_obj.attributes.updated_at, datetime)
    assert isinstance(response_obj.attributes.brands[0].combined_average_price, float)
