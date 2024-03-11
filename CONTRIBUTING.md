### Contributing to the Jungle Scout Python SDK

We welcome contributions from the community. Please read the following guidelines before contributing to the project.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) (3.7+)
- [Pyenv](https://github.com/pyenv/pyenv)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Tox](https://tox.readthedocs.io/en/latest/)
- [ruff](https://github.com/astral-sh/ruff)

### Project Setup and Running Tests

```bash
# install supported versions of python
pyenv install

# install packaging and build tools
pipx install tox
pipx install poetry

# install project dependencies
poetry install

# run typechecking
tox run -e typecheck
```

To run editable modle, use the following command:

```bash
  pip install -e .
```

### Testing

We use [pytest](https://docs.pytest.org/en/stable/) for testing. To run the tests, use the following command:

```bash
    # complete test run on the supported python versions
    tox run

    # run tests on a specific tag
    poetry run pytest tests -m "not integration"
```

When running integration tests, don't forget to set the following environment variables in a `.env.test` file:

```bash
API_KEY_NAME="api_key_name"
API_KEY="api_key"
```

Remember that those WILL consume your API credits.

### Code Formatting

This project uses [black](https://pypi.org/project/black/) for code formatting, [isort](https://pypi.org/project/isort/) for import sorting and [ruff](https://github.com/astral-sh/ruff) as a linter. If you are using VSCode, you can install the following extensions:

- [black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
- [ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

You'd also need to add the following settings to your `settings.json`:

```json
 "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true,
      "source.fixAll": true
    }
  },
  "isort.args": ["--profile", "black"]
```

### Pydantic Models

This project defines API model objects using
[Pydantic](https://docs.pydantic.dev/latest). Autocomplete for model parameters
during instantiation should work by default in most modern IDEs. For Jetbrains
IDEs, the [Pydantic](https://plugins.jetbrains.com/plugin/12861-pydantic) plugin
is required for autocomplete. See the following links for more information:

- [pydantic/pull/2721](https://github.com/pydantic/pydantic/pull/2721)
- [pydantic/issues/650](https://github.com/pydantic/pydantic/issues/650)
