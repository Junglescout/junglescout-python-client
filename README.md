# Jungle Scout Python Client

The official Jungle Scout API Python Client with both sync and async support.
Documentation for this client is available on
[Read the Docs](https://jungle-scout-junglescout-python-client.readthedocs-hosted.com).

See the [Jungle Scout API Documentation](https://developer.junglescout.com) and
the [Jungle Scout Postman Collection](https://postman.junglescout.com) for more
information about the Jungle Scout API.

## Rate Limits

The current API request limit per minute is 300, and our burst limit per second is 15.

## Installation

```bash
pip install junglescout-client
```

## Usage

Here's a quick example using sync client to get keywords by ASIN:

```python
from junglescout import ClientSync
from junglescout.models.parameters import Marketplace, ApiType, FilterOptions, Sort

API_KEY_NAME = "api_key_name"
API_KEY = "api_key"

client = ClientSync(
    api_key_name=API_KEY_NAME,
    api_key=API_KEY,
    marketplace=Marketplace.US,
    api_type=ApiType.JS
)

filter_options = FilterOptions(min_monthly_search_volume_exact=150)

keywords = client.keywords_by_asin(
    asin='B005IHSKYS',
    filter_options=filter_options,
    sort_option=Sort.MONTHLY_SEARCH_VOLUME_EXACT_MATCH
)

client.close()
```

See the
[documentation](https://jungle-scout-junglescout-python-client.readthedocs-hosted.com)
for information on the available methods and parameters.

### Pydantic Models

This project defines API model objects using
[Pydantic](https://docs.pydantic.dev/latest). Autocomplete for model parameters
during instantiation should work by default in most modern IDEs. For Jetbrains
IDEs, the [Pydantic](https://plugins.jetbrains.com/plugin/12861-pydantic) plugin
is required for autocomplete. See the following links for more information:

- [pydantic/pull/2721](https://github.com/pydantic/pydantic/pull/2721)
- [pydantic/issues/650](https://github.com/pydantic/pydantic/issues/650)

## Contributing

Contributions are welcome! Please read the
[contributing guidelines](CONTRIBUTING.md) for more information.
