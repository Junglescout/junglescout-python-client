import factory
from faker import Faker

fake = Faker()


class AttributesFactory(factory.DictFactory):
    estimated_30_day_search_volume = factory.LazyAttribute(lambda _: fake.random_int(min=1, max=100))
    exact_suggested_bid_median = factory.LazyAttribute(lambda _: fake.random_int(min=1, max=100))
    product_count = factory.LazyAttribute(lambda _: fake.random_int(min=1, max=100))
    updated_at = factory.LazyAttribute(lambda _: fake.date_time_this_year().isoformat())
    brands = factory.LazyAttribute(
        lambda: [
            {
                "brand": fake.company(),
                "combined_products": fake.random_int(min=1, max=100),
                "combined_weighted_sov": fake.random_int(min=1, max=100),
                "combined_basic_sov": fake.random_int(min=1, max=100),
                "combined_average_position": fake.random_int(min=1, max=100),
                "combined_average_price": fake.random_int(min=1, max=100),
                "organic_products": fake.random_int(min=1, max=100),
                "organic_weighted_sov": fake.random_int(min=1, max=100),
                "organic_basic_sov": fake.random_int(min=1, max=100),
                "organic_average_position": fake.random_int(min=1, max=100),
                "organic_average_price": fake.random_int(min=1, max=100),
                "sponsored_products": fake.random_int(min=1, max=100),
                "sponsored_weighted_sov": fake.random_int(min=1, max=100),
                "sponsored_basic_sov": fake.random_int(min=1, max=100),
                "sponsored_average_position": fake.random_int(min=1, max=100),
                "sponsored_average_price": fake.random_int(min=1, max=100),
            }
            for _ in range(4)
        ]
    )
    top_asins = factory.LazyAttribute(
        lambda: [
            {
                "asin": fake.bothify(text="us/B0####???"),
                "name": fake.name(),
                "brand": fake.company(),
                "clicks": fake.random_int(min=1, max=100),
                "conversions": fake.random_int(min=1, max=100),
                "conversion_rate": fake.random_int(min=1, max=100),
            }
            for _ in range(5)
        ]
    )
    top_asins_model_start_date = factory.LazyAttribute(lambda: fake.date_time_this_year().isoformat())
    top_asins_model_end_date = factory.LazyAttribute(lambda: fake.date_time_this_year().isoformat())


class ShareOfVoiceResponseFactory(factory.DictFactory):
    data = factory.Dict(
        {
            "type": "this_type",
            "id": fake.bothify(text="us/B0####???"),
            "attributes": AttributesFactory(),
        }
    )


def generate_share_of_voice_responses():
    return ShareOfVoiceResponseFactory()
