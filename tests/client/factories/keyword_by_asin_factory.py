from typing import Dict, List

import factory
from faker import Faker

fake = Faker()


class AttributesFactory(factory.Factory):
    class Meta:
        model = dict

    country = "us"
    name = fake.name()
    primary_asin = fake.bothify(text="B0####???")
    monthly_trend = fake.random_int(min=0, max=100)
    monthly_search_volume_exact = fake.random_int(min=0, max=100)
    quarterly_trend = fake.random_int(min=0, max=100)
    monthly_search_volume_broad = fake.random_int(min=0, max=100)
    dominant_category = fake.name()
    recommended_promotions = fake.name()
    sp_brand_ad_bid = fake.name()
    ppc_bid_broad = fake.name()
    ppc_bid_exact = fake.name()
    ease_of_ranking_score = fake.name()
    relevancy_score = fake.name()
    organic_product_count = fake.name()
    sponsored_product_count = fake.name()
    updated_at = fake.date_time_this_year().isoformat()
    organic_rank = fake.name()
    sponsored_rank = fake.name()
    overall_rank = fake.name()
    organic_ranking_asins_count = fake.name()
    sponsored_ranking_asins_count = fake.name()
    avg_competitor_organic_rank = fake.name()
    avg_competitor_sponsored_rank = fake.name()
    relative_organic_position = fake.name()
    relative_sponsored_position = fake.name()
    competitor_organic_rank = fake.name()
    variation_lowest_organic_rank = fake.name()


class KeywordsByAsinResponseFactory(factory.DictFactory):
    class Meta:
        model = dict

    type = "this_type"
    id = fake.bothify(text="us/B0####???")
    attributes = factory.SubFactory(AttributesFactory)


def generate_keywords_by_asin_responses(length: int = 1) -> List[Dict]:
    return [KeywordsByAsinResponseFactory() for _ in range(length)]
