# jungle-scout-python-client

Jungle Scout API Python Client.

## Installation

```bash
# install using Github personal access token for authentication
pip install git+https://${GITHUB_PERSONAL_TOKEN}@github.com/Junglescout/jungle-scout-python-client.git@main
```

## Usage

```python
from jungle_scout.client import Client
from jungle_scout.models.parameters.marketplace import Marketplace

API_KEY_NAME = "api_key_name"
API_KEY = "api_key"

client = Client(api_key_name=API_KEY_NAME, api_key=API_KEY, marketplace=Marketplace.US)

keywords = client.keywords_by_asin('B005IHSKYS')
```

### Pydantic Models

Notes to get autocomplete working when creating models.
https://github.com/pydantic/pydantic/pull/2721
https://github.com/pydantic/pydantic/issues/650





## Development

### Running Tests

```bash
# install tox
pipx install tox

# install poetry
pipx install poetry

# install project python versions
pyenv install

# install dependencies
poetry install

# run tests
tox run
```
