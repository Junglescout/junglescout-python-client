from typing import Any

import factory
from faker import Faker

fake = Faker()


class AttributesFactory(factory.DictFactory):
    country = "us"
    name = fake.name()
    monthly_trend = fake.random_int(min=0, max=100)
    monthly_search_volume_exact = fake.random_int(min=0, max=100)
    quarterly_trend = fake.random_int(min=0, max=100)
    monthly_search_volume_broad = fake.random_int(min=0, max=100)
    dominant_category = fake.name()
    recommended_promotions = fake.random_int(min=0, max=100)
    sp_brand_ad_bid = fake.random_int()
    ppc_bid_broad = fake.random_int()
    ppc_bid_exact = fake.random_int()
    ease_of_ranking_score = fake.random_int()
    relevancy_score = fake.random_int()
    organic_product_count = fake.random_int()
    sponsored_product_count = fake.random_int()


class LinksFactory(factory.DictFactory):
    self = fake.uri()
    next = fake.uri()


class KeywordsByKeywordResponseFactory(factory.DictFactory):
    class Params:
        total_items = 1

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
    links = factory.LazyAttribute(lambda _: LinksFactory())
    meta = factory.LazyAttribute(lambda o: {"total_items": o.total_items})


def generate_keywords_by_keyword_responses(total_items: int = 1) -> dict[str, Any]:
    return KeywordsByKeywordResponseFactory(total_items=total_items)
