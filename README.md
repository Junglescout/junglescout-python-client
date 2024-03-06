# jungle-scout-python-client

The official Jungle Scout API Python Client.

## Usage

This project uses [black](https://pypi.org/project/black/) for code formatting, [isort](https://pypi.org/project/isort/) for import sorting. If you are using VSCode, you can install the following extensions:

- [black](https://marketplace.visualstudio.com/items?itemName=ms-python.black)
- [isort](https://marketplace.visualstudio.com/items?itemName=pycqa.isort)

You'd also need to add the following settings to your `settings.json`:

```json
 "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  },
  "isort.args": ["--profile", "black"]
```

## Installation

```bash
# TODO: remove the personal access token when this project is published to pypi
# while this repository is still private, install
# using Github personal access token for authentication
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

This project defines API model objects using
[Pydantic](https://docs.pydantic.dev/latest). Autocomplete for model parameters
during instantiation should work by default in most modern IDEs. For Jetbrains
IDEs, the [Pydantic](https://plugins.jetbrains.com/plugin/12861-pydantic) plugin
is required for autocomplete. See the following links for more information:

- [pydantic/pull/2721](https://github.com/pydantic/pydantic/pull/2721)
- [pydantic/issues/650](https://github.com/pydantic/pydantic/issues/650)

## Development

### Project Setup and Running Tests

```bash
# install supported versions of python
pyenv install

# install packaging and build tools
pipx install tox
pipx install poetry

# install project dependencies
poetry install

# run tests
tox run
```
