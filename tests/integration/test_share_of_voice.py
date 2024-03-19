import pytest

from junglescout.client import Client
from junglescout.models.parameters import Marketplace


@pytest.mark.integration()
def test_share_of_voice(api_keys):
    client = Client(**api_keys, marketplace=Marketplace.US)
    response = client.share_of_voice(keyword="yoga mat", marketplace=Marketplace.US)
    assert response.data is not None
