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

See :class:`junglescout.client.Client` for more information about authenticating with the Jungle Scout API.

Making Your First Request
=========================

All requests to the Jungle Scout API are made using the :class:`junglescout.client.Client` class. This class
provides a simple interface for making requests to the Jungle Scout API. The following example demonstrates how to
make a request to the Jungle Scout API using the Python client.

.. code-block:: python

    from junglescout.client import Client
    from junglescout.models.parameters import (
        Marketplace,
    )

    API_KEY_NAME = "API_KEY_NAME"
    API_KEY = "API_KEY"

    client = Client(api_key_name=API_KEY_NAME, api_key=API_KEY, marketplace=Marketplace.US)

    keywords_by_asin = client.keywords_by_asin(
        asin=["B0CP9Z56SW", "B0154ASID6"],
    )

See the :class:`junglescout.client.Client` class for more information about making requests to the Jungle Scout API.

Analyzing the Response
======================

Responses from the Jungle Scout API are returned as instances of...

Rate Limiting
=============

The Jungle Scout API enforces rate limits as following: 300 requests per minute or 15 requests per second. If you exceed the rate limit, you will receive a 429 status code in response to your request.

What's Next?
============

- See :doc:`examples/index` for code examples and use cases.
- See :doc:`api` for information about all available endpoints and parameters.
