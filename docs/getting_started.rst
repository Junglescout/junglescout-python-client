===============
Getting Started
===============

Authentication
==============

The Jungle Scout Python Client requires an API key to authenticate with the Jungle Scout API.

.. important::
    See the :js_api_docs:`Authentication <api#authentication>` section of the Jungle Scout API documentation
    for more information about authenticating with the API.

Making Your First Request
=========================

All requests to the Jungle Scout API are made using ether the :class:`~junglescout.client_sync.ClientSync` or
:class:`~junglescout.client_async.ClientAsync` class. These classes provide simple interfaces for making requests to the
Jungle Scout API. The following example demonstrates how to make a request to the Jungle Scout API using the
sync client.

.. code-block:: python

    from junglescout import ClientSync
    from junglescout.models.parameters import (
        Marketplace,
    )

    API_KEY_NAME = "API_KEY_NAME"
    API_KEY = "API_KEY"

    client = ClientSync(api_key_name=API_KEY_NAME, api_key=API_KEY, marketplace=Marketplace.US)

    keywords_by_asin = client.keywords_by_asin(
        asin=["B0CP9Z56SW", "B0154ASID6"],
    )

Analyzing the Response
======================

Responses from the Jungle Scout API are returned as :pydantic:`Pydantic <>` models. See
:mod:`junglescout.models.responses` for response models.

What's Next?
============

- See :doc:`examples/index` for code examples and use cases.
- See :doc:`api` for information about all available endpoints and parameters.
