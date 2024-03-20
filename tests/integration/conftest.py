import os

import pytest


@pytest.fixture(scope="package")
def api_keys():
    return {
        "api_key_name": os.environ["API_KEY_NAME"],
        "api_key": os.environ["API_KEY"],
    }
