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

### Creating Local Development Environment

```bash
# its recommended to install the project in a virtual environment for local development
# the example commands use `pyenv virtualenv` to create the virtual environment
# see https://github.com/pyenv/pyenv-virtualenv for more information
pyenv virtualenv 3.8 jungle-scout-python-client-3.8
pyenv activate jungle-scout-python-client-3.8

# install project in editable mode with dev dependencies in the virtual environment
pip install -e .[dev]
```
