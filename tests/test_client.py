from jungle_scout.client import Client

API_KEY_NAME = "api_key_name"
API_KEY = "api_key"


def test_can_instantiate():
    client = Client(api_key_name=API_KEY_NAME, api_key=API_KEY)
    assert isinstance(client, Client)
