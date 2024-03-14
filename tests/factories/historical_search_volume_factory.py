import factory
from faker import Faker

fake = Faker()


class AttributesFactory(factory.DictFactory):
    estimate_start_date = fake.date_this_year().isoformat()
    estimate_end_date = fake.date_this_year().isoformat()
    estimated_exact_search_volume = fake.random_int(min=0, max=100)


class HistoricalSearchVolumeResponseFactory(factory.DictFactory):
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


def generate_historical_search_volume_responses(total_items: int = 1):
    return HistoricalSearchVolumeResponseFactory(total_items=total_items)
