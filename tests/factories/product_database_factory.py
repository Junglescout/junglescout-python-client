from typing import Any

import factory
from faker import Faker

fake = Faker()


class AttributesFactory(factory.DictFactory):
    title = factory.Faker("sentence")
    price = factory.Faker("pyfloat", positive=True)
    reviews = factory.Faker("pyint")
    category = factory.Faker("sentence")
    rating = factory.Faker("pyfloat", positive=True)
    image_url = factory.Faker("image_url")
    parent_asin = factory.Faker("bothify", text="B0####???")
    is_variant = factory.Faker("boolean")
    seller_type = factory.Faker("sentence")
    variants = factory.List([fake.bothify(text="B0####???") for _ in range(2)])
    is_standalone = factory.Faker("boolean")
    is_parent = factory.Faker("boolean")
    brand = factory.Faker("sentence")
    product_rank = factory.Faker("pyint")
    weight_value = factory.Faker("pyfloat", positive=True)
    weight_unit = factory.Faker("sentence")
    length_value = factory.Faker("pyfloat", positive=True)
    width_value = factory.Faker("pyfloat", positive=True)
    height_value = factory.Faker("pyfloat", positive=True)
    dimensions_unit = factory.Faker("sentence")
    listing_quality_score = factory.Faker("pyfloat", positive=True)
    number_of_sellers = factory.Faker("pyint")
    buy_box_owner = factory.Faker("sentence")
    buy_box_owner_seller_id = factory.Faker("bothify", text="B0####???")
    date_first_available = factory.Faker("date")
    date_first_available_is_estimated = factory.Faker("boolean")
    approximate_30_day_revenue = factory.Faker("pyfloat", positive=True)
    approximate_30_day_units_sold = factory.Faker("pyint")
    ean_list = factory.List([fake.random_int(min=0, max=100) for _ in range(2)])
    isbn_list = factory.List([fake.isbn13() if fake.boolean() else fake.isbn10() for _ in range(2)])
    upc_list = factory.List([fake.random_int(min=0, max=100) for _ in range(2)])
    gtin_list = factory.List([fake.random_int(min=0, max=100) for _ in range(2)])
    variant_reviews = factory.Faker("pyint")
    updated_at = fake.date_time_this_year().isoformat()
    subcategory_ranks = factory.List([{"subcategory": fake.name(), "rank": fake.random_int(min=0, max=100)}])
    fee_breakdown = factory.Dict(
        {
            "fba_fee": fake.random_int(min=0, max=100),
            "referral_fee": fake.random_int(min=0, max=100),
            "variable_closing_fee": fake.random_int(min=0, max=100),
            "total_fees": fake.random_int(min=0, max=100),
        }
    )


class LinksFactory(factory.DictFactory):
    self = fake.uri()
    next = fake.uri()


class ProductDatabaseResponseFactory(factory.DictFactory):
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


def generate_product_database_responses(total_items: int = 1) -> dict[str, Any]:
    return ProductDatabaseResponseFactory(total_items=total_items)
