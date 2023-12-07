from jungle_scout.client import Client


def test_can_instantiate():
    client = Client()
    assert isinstance(client, Client)
