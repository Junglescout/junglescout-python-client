from jungle_scout.client import Client
from jungle_scout.models.parameters.marketplace import Marketplace

API_KEY_NAME = "api_key_name"
API_KEY = "api_key"


def test_can_instantiate():
    client = Client(api_key_name=API_KEY_NAME, api_key=API_KEY)
    assert isinstance(client, Client)


def test_can_instantiate_with_marketplace():
    client = Client(api_key_name=API_KEY_NAME, api_key=API_KEY, marketplace=Marketplace.US)
    assert isinstance(client, Client)
    assert client.marketplace == Marketplace.US
