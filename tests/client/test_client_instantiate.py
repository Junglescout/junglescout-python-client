import os

import pytest

from jungle_scout.client import Client
from jungle_scout.models.parameters import Marketplace


@pytest.fixture
def credentials():
    return {
        "api_key_name": os.environ["API_KEY_NAME"],
        "api_key": os.environ["API_KEY"],
    }


def test_can_instantiate(credentials):
    client = Client(**credentials)
    assert isinstance(client, Client)


def test_can_instantiate_with_marketplace(credentials):
    client = Client(marketplace=Marketplace.US, **credentials)
    assert isinstance(client, Client)
    assert client.marketplace == Marketplace.US
