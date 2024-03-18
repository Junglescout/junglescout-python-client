import json
from jungle_scout.models.responses.keyword_by_keyword import KeywordByKeyword


def test_keyword_by_keyword():
    response_obj = KeywordByKeyword.model_validate_json(
        json.dumps(
            {
                "links": "links",
                "meta": "meta",
                "id": "123",
                "type": "foo",
                "attributes": {
                    "country": "foo",
                    "name": "foo",
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
                },
            }
        )
    )
    assert isinstance(response_obj, KeywordByKeyword)
