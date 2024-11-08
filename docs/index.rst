##########################
Jungle Scout Python Client
##########################

This is a Python client for the :js_api_docs:`Jungle Scout API <api>` which provides which provides sync and
async interfaces.

.. important::
    See the :js_api_docs:`Jungle Scout API reference <api>` for more information about the
    available endpoints and their parameters. Information about the Jungle Scout API is also
    available in a :js_postman:`Postman collection <>`.

##########
Quickstart
##########

Install the Jungle Scout Python client.

.. code-block:: bash

    pip install junglescout-client

Import the client and create an instance.

.. code-block:: python

    from junglescout import ClientSync
    from junglescout.models.parameters import (
        Marketplace,
    )

    API_KEY_NAME = "API_KEY_NAME"
    API_KEY = "API_KEY"
    client = ClientSync(api_key_name=API_KEY_NAME, api_key=API_KEY, marketplace=Marketplace.US)


Make a request to the API.

.. code-block:: python

    keywords_by_asin = client.keywords_by_asin(
        asin=["B0CP9Z56SW", "B0154ASID6"],
    )

#############
Documentation
#############

The :doc:`getting_started` section provides a quick overview of how to install and use the
Jungle Scout Python client. See the :doc:`examples/index` section for more code examples of
common use cases. The :doc:`api` section provides detailed information about the available
endpoints and their parameters.

.. toctree::
    :maxdepth: 2

    getting_started
    examples/index
    api

##################
Indices and Tables
##################

-  :ref:`genindex`
-  :ref:`modindex`
-  :ref:`search`
