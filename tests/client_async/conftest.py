import pytest

from junglescout import ClientAsync
from junglescout.models.parameters import Marketplace


@pytest.fixture(scope="package")
def client_async():
    return ClientAsync(api_key_name="fake_api_key_name", api_key="fake_api_key", marketplace=Marketplace.US)
