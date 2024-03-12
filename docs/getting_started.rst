===============
Getting Started
===============

Authentication
==============

The Jungle Scout Python Client requires an API key to authenticate with the Jungle Scout API. You can
generate an API key by visiting the ...

.. important::
    See the :js_api_docs:`Authentication <api#authentication>` section of the Jungle Scout API documentation
    for more information about authenticating with the API.

See :class:`jungle_scout.client.Client` for more information about authenticating with the Jungle Scout API.

Making Your First Request
=========================

All requests to the Jungle Scout API are made using the :class:`jungle_scout.client.Client` class. This class
provides a simple interface for making requests to the Jungle Scout API. The following example demonstrates how to
make a request to the Jungle Scout API using the Python client.

.. code-block:: python

    from jungle_scout.client import Client
    from jungle_scout.models.parameters import (
        Marketplace,
    )

    API_KEY_NAME = "API_KEY_NAME"
    API_KEY = "API_KEY"

    client = Client(api_key_name=API_KEY_NAME, api_key=API_KEY, marketplace=Marketplace.US)

    keywords_by_asin = client.keywords_by_asin(
        asin=["B0CP9Z56SW", "B0154ASID6"],
    )

See the :class:`jungle_scout.client.Client` class for more information about making requests to the Jungle Scout API.

Analyzing the Response
======================

Responses from the Jungle Scout API are returned as instances of...

What's Next?
============

- See :doc:`examples/index` for code examples and use cases.
- See :doc:`api` for information about all available endpoints and parameters.
