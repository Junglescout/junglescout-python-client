import json
from datetime import datetime

from jungle_scout.models.responses.product_database import ProductDatabase


def test_product_database():
    response_obj = ProductDatabase.model_validate_json(
        json.dumps(
            {
                "id": "123",
                "type": "foo",
                "attributes": {
                    "title": "foo",
                    "price": 1,
                    "reviews": 1,
                    "category": "foo",
                    "rating": 1,
                    "image_url": "foo",
                    "parent_asin": "foo",
                    "is_variant": True,
                    "seller_type": "foo",
                    "variants": 1,
                    "is_standalone": True,
                    "is_parent": True,
                    "brand": "foo",
                    "product_rank": 1,
                    "weight_value": 1,
                    "weight_unit": "foo",
                    "length_value": 1,
                    "width_value": 1,
                    "height_value": 1,
                    "dimensions_unit": "foo",
                    "listing_quality_score": 1,
                    "number_of_sellers": 1,
                    "buy_box_owner": "foo",
                    "buy_box_owner_seller_id": "foo",
                    "date_first_available": "2024-11-05",
                    "date_first_available_is_estimated": True,
                    "approximate_30_day_revenue": 1,
                    "approximate_30_day_units_sold": 1,
                    "ean_list": [1, 2],
                    "variant_reviews": 1,
                    "updated_at": "2024-11-05",
                    "subcategory_ranks": [{"subcategory": 1, "rank": 1}],
                    "fee_breakdown": {"fba_fee": 1, "referral_fee": 1, "variable_closing_fee": 1, "total_fees": 1},
                },
            }
        )
    )
    assert isinstance(response_obj, ProductDatabase)
    assert isinstance(response_obj.attributes.date_first_available, datetime)
    assert isinstance(response_obj.attributes.updated_at, datetime)
    assert isinstance(response_obj.attributes.is_parent, bool)
