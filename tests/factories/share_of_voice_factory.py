import factory
from faker import Faker

fake = Faker()


class AttributesFactory(factory.DictFactory):
    class Params:
        top_asins_count = 5
        brands_count = 4

    estimated_30_day_search_volume = fake.random_int(min=1, max=100)
    exact_suggested_bid_median = fake.random_int(min=1, max=100)
    product_count = fake.random_int(min=1, max=100)
    updated_at = fake.date_time_this_year().isoformat()
    brands = factory.LazyAttribute(
        lambda o: [
            {
                "brand": fake.company(),
                "combined_products": fake.random_int(min=1, max=100),
                "combined_weighted_sov": fake.random_int(min=1, max=100),
                "combined_basic_sov": fake.random_int(min=1, max=100),
                "combined_average_position": fake.random_int(min=1, max=100),
                "combined_average_price": fake.pyfloat(),
                "organic_products": fake.random_int(min=1, max=100),
                "organic_weighted_sov": fake.random_int(min=1, max=100),
                "organic_basic_sov": fake.random_int(min=1, max=100),
                "organic_average_position": fake.random_int(min=1, max=100),
                "organic_average_price": fake.pyfloat(),
                "sponsored_products": fake.random_int(min=1, max=100),
                "sponsored_weighted_sov": fake.random_int(min=1, max=100),
                "sponsored_basic_sov": fake.random_int(min=1, max=100),
                "sponsored_average_position": fake.random_int(min=1, max=100),
                "sponsored_average_price": fake.pyfloat(),
            }
            for _each in range(o.brands_count)
        ]
    )
    top_asins = factory.LazyAttribute(
        lambda o: [
            {
                "asin": fake.bothify(text="us/B0####???"),
                "name": fake.name(),
                "brand": fake.company(),
                "clicks": fake.random_int(min=1, max=100),
                "conversions": fake.random_int(min=1, max=100),
                "conversion_rate": fake.pyfloat(),
            }
            for _each in range(o.top_asins_count)
        ]
    )
    top_asins_model_start_date = fake.date_time_this_year().isoformat()
    top_asins_model_end_date = fake.date_time_this_year().isoformat()


class ShareOfVoiceResponseFactory(factory.DictFactory):
    class Params:
        top_asins_count = 5
        brands_count = 4

    data = factory.LazyAttribute(
        lambda o: {
            "type": "this_type",
            "id": fake.bothify(text="us/B0####???"),
            "attributes": AttributesFactory(top_asins_count=o.top_asins_count, brands_count=o.brands_count),
        }
    )


def generate_share_of_voice_responses(top_asins_count: int = 5, brands_count: int = 4):
    return ShareOfVoiceResponseFactory(top_asins_count=top_asins_count, brands_count=brands_count)
