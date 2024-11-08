##########################
Closing Client Connections
##########################

Context Manager
===============

Both :class:`~junglescout.client_sync.ClientSync` and :class:`~junglescout.client_async.ClientAsync` clients can be
used as context manager. This ensures that the client is properly closed and resources are released when the context
manager exits.

**Synchronous Example**

.. code-block:: python

    from junglescout import ClientSync
    from junglescout.models.parameters import (
        Marketplace,
    )

    API_KEY_NAME = "API_KEY_NAME"
    API_KEY = "API_KEY"

    with ClientSync(
        api_key_name=API_KEY_NAME,
        api_key=API_KEY,
        marketplace=Marketplace.US,
    ) as client:
        keywords_by_asin = client.keywords_by_asin(
            asin=["B0CP9Z56SW", "B0154ASID6"],
        )

    assert client.is_closed


**Asynchronous Example**

.. code-block:: python

    import asyncio

    from junglescout import ClientAsync
    from junglescout.models.parameters import (
        Marketplace,
    )

    API_KEY_NAME = "API_KEY_NAME"
    API_KEY = "API_KEY"

    async def example_coroutine():
        async with ClientAsync(
            api_key_name=API_KEY_NAME,
            api_key=API_KEY,
            marketplace=Marketplace.US,
        ) as client:
            return await client.keywords_by_asin(
                asin=["B0CP9Z56SW", "B0154ASID6"],
            )
        assert client.is_closed


    keywords_by_asin = asyncio.run(example_coroutine())

Explicit Close
==============

Clients can also be closed explicitly by calling the :meth:`~junglescout.client_sync.ClientSync.close` method on both
:class:`~junglescout.client_sync.ClientSync` and :class:`~junglescout.client_async.ClientAsync` clients.

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
    client.close()
    assert client.is_closed
