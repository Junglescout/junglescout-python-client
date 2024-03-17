import factory
from faker import Faker

fake = Faker()


class AttributesFactory(factory.DictFactory):
    asin = fake.bothify(text="B0####???")
    is_parent = fake.boolean()
    is_variant = fake.boolean()
    is_standalone = fake.boolean()
    parent_asin = fake.bothify(text="B0####???")
    variants = fake.random_int(min=0, max=100)
    data = factory.LazyAttribute(
        lambda: [
            {
                "date": fake.date_this_year().isoformat(),
                "estimated_units_sold": fake.random_int(min=0, max=100),
                "last_known_price": fake.random_int(min=0, max=100),
            }
            for _ in range(3)
        ]
    )


class SalesEstimatesResponseFactory(factory.DictFactory):
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


def generate_sales_estimates_responses(total_items: int = 1, data_items: int = 3):
    return SalesEstimatesResponseFactory(total_items=total_items, data_items=data_items)
