from typing import Any, List

import factory
from faker import Faker

fake = Faker()


class AttributesFactory(factory.DictFactory):
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
    total_items = factory.Faker("pyint")

    data = factory.LazyAttribute(
        lambda o: [
            {
                "type": "this_type",
                "id": fake.bothify(text="us/B0####???"),
                "attributes": AttributesFactory(),
            }
            for _ in range(o.total_items)
        ]
    )
    links = {"self": fake.uri(), "next": fake.uri()}
    meta = factory.LazyAttribute(lambda o: {"total_items": o.total_items})


def generate_keywords_by_asin_responses(total_items: int = 1) -> List[Any]:
    return KeywordsByAsinResponseFactory(total_items=total_items)
