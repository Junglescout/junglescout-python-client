##########################
Closing Client Connections
##########################

Context Manager
===============

Both :class:`~junglescout.client_sync.ClientSync` and :class:`~junglescout.client_async.ClientAsync` clients can be
used as context manager. This ensures that the client is properly closed and resources are released when the context
manager exits.

.. code-block:: python

    from junglescout.client import ClientSync
    from junglescout.models.parameters import (
        Marketplace,
    )

    API_KEY_NAME = "API_KEY_NAME"
    API_KEY = "API_KEY"

    with ClientSync(api_key_name=API_KEY_NAME, api_key=API_KEY, marketplace=Marketplace.US) as client:
        keywords_by_asin = client.keywords_by_asin(
            asin=["B0CP9Z56SW", "B0154ASID6"],
        )

Explicit Close
==============

Clients can also be closed explicitly by calling the :meth:`~junglescout.client_sync.ClientSync.close` method.

.. code-block:: python

    from junglescout.client import ClientSync
    from junglescout.models.parameters import (
        Marketplace,
    )

    API_KEY_NAME = "API_KEY_NAME"
    API_KEY = "API_KEY"

    client = ClientSync(api_key_name=API_KEY_NAME, api_key=API_KEY, marketplace=Marketplace.US)
    keywords_by_asin = client.keywords_by_asin(
        asin=["B0CP9Z56SW", "B0154ASID6"],
    )
    client.close()
