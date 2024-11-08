#############
Async Support
#############

The Jungle Scout API client supports asynchronous operations using the :class:`~junglescout.client_async.ClientAsync`
client.

.. code-block:: python

    from junglescout.client import ClientAsync
    from junglescout.models.parameters import (
        Marketplace,
    )

    API_KEY_NAME = "API_KEY_NAME"
    API_KEY = "API_KEY"

    async def example_coroutine():
        async with ClientAsync(api_key_name=API_KEY_NAME, api_key=API_KEY, marketplace=Marketplace.US) as client:
            keywords_by_asin = await client.keywords_by_asin(
                asin=["B0CP9Z56SW", "B0154ASID6"],
            )

.. note::
    The Jungle Scout Python client uses :httpx:`HTTPX <>` under the hood for making async HTTP requests. In order to get
    the most benefit from connection pooling, make sure you're not instantiating multiple client instances. For
    example by using `async with` inside a "hot loop". This can be achieved either by having a single scoped client
    that's passed throughout wherever it's needed, or by having a single global client instance. See the
    :httpx:`HTTPX async <async>` guide for more information.

