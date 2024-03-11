# Jungle Scout Python Client

The official Jungle Scout API Python Client. You can learn more about the Jungle Scout API [here](https://developer.junglescout.com/) and our official [Postman collection](https://postman.junglescout.com/)

## Usage

This project uses [black](https://pypi.org/project/black/) for code formatting, [isort](https://pypi.org/project/isort/) for import sorting.

## Installation

```bash
# TODO: remove the personal access token when this project is published to pypi
# while this repository is still private, install
# using Github personal access token for authentication
pip install git+https://${GITHUB_PERSONAL_TOKEN}@github.com/Junglescout/jungle-scout-python-client.git@main
```

## Usage

Our API is designed to be simple and easy to use. Here's a quick example of how to use the client to get keywords by ASIN:

```python
from jungle_scout.client import Client
from jungle_scout.models.parameters import Marketplace, ApiType, FilterOptions

API_KEY_NAME = "api_key_name"
API_KEY = "api_key"

client = Client(api_key_name=API_KEY_NAME, api_key=API_KEY, marketplace=Marketplace.US, api_type=ApiType.JS)

filter_options = FilterOptions(min_monthly_search_volume_exact=150)

keywords = client.keywords_by_asin(asin='B005IHSKYS', filter_options=filter_options, sort_option=Sort.MONTHLY_SEARCH_VOLUME_EXACT_MATCH)
```

All our API methods are available in the `Client` class. You can find the full list of available methods in the [API documentation](https://developer.junglescout.com/). Filter options and sort options are available as enums in the `jungle_scout.models.parameters` module.

You can see more examples in the [examples](examples) directory.

### Pydantic Models

This project defines API model objects using
[Pydantic](https://docs.pydantic.dev/latest). Autocomplete for model parameters
during instantiation should work by default in most modern IDEs. For Jetbrains
IDEs, the [Pydantic](https://plugins.jetbrains.com/plugin/12861-pydantic) plugin
is required for autocomplete. See the following links for more information:

- [pydantic/pull/2721](https://github.com/pydantic/pydantic/pull/2721)
- [pydantic/issues/650](https://github.com/pydantic/pydantic/issues/650)

## Contributing

Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) for more information.
