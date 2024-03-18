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
    sp_brand_ad_bid = fake.random_int()
    ppc_bid_broad = fake.random_int()
    ppc_bid_exact = fake.random_int()
    ease_of_ranking_score = fake.random_int()
    relevancy_score = fake.random_int()
    organic_product_count = fake.random_int()
    sponsored_product_count = fake.random_int()
    updated_at = fake.date_time_this_year().isoformat()
    organic_rank = fake.random_int()
    sponsored_rank = fake.random_int()
    overall_rank = fake.random_int()
    organic_ranking_asins_count = fake.random_int()
    sponsored_ranking_asins_count = fake.random_int()
    avg_competitor_organic_rank = fake.random_int()
    avg_competitor_sponsored_rank = fake.random_int()
    relative_organic_position = fake.random_int()
    relative_sponsored_position = fake.random_int()
    competitor_organic_rank = fake.random_int()
    variation_lowest_organic_rank = fake.random_int()


class LinksFactory(factory.DictFactory):
    self = fake.uri()
    next = fake.uri()


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
    links = factory.LazyAttribute(lambda _: LinksFactory())
    meta = factory.LazyAttribute(lambda o: {"total_items": o.total_items})


def generate_keywords_by_asin_responses(total_items: int = 1) -> dict:
    return KeywordsByAsinResponseFactory(total_items=total_items)
