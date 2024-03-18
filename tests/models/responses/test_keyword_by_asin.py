import json
from datetime import datetime

from jungle_scout.models.responses.keyword_by_asin import KeywordByASIN


def test_keyword_by_asin():
    response_obj = KeywordByASIN.model_validate_json(
        json.dumps(
            {
                "id": "foo",
                "type": "foo",
                "attributes": {
                    "country": "foo",
                    "name": "foo",
                    "primary_asin": "foo",
                    "monthly_trend": 1,
                    "monthly_search_volume_exact": 1,
                    "quarterly_trend": 1,
                    "monthly_search_volume_broad": 1,
                    "dominant_category": "foo",
                    "recommended_promotions": "foo",
                    "sp_brand_ad_bid": 1,
                    "ppc_bid_broad": 1,
                    "ppc_bid_exact": 1,
                    "ease_of_ranking_score": 1,
                    "relevancy_score": 1,
                    "organic_product_count": 1,
                    "sponsored_product_count": 1,
                    "updated_at": "2024-11-05",
                    "organic_rank": 1,
                    "sponsored_rank": 1,
                    "overall_rank": 1,
                    "organic_ranking_asins_count": 1,
                    "sponsored_ranking_asins_count": 1,
                    "avg_competitor_organic_rank": 1,
                    "avg_competitor_sponsored_rank": 1,
                    "relative_organic_position": 1,
                    "relative_sponsored_position": 1,
                    "competitor_organic_rank": 1,
                    "variation_lowest_organic_rank": 1,
                },
            }
        )
    )
    assert isinstance(response_obj, KeywordByASIN)
    assert isinstance(response_obj.attributes.updated_at, datetime)
