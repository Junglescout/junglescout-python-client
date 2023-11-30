### Contributing to the Jungle Scout Python SDK

We welcome contributions from the community. Please read the following guidelines before contributing to the project.

## Getting Started

### Project Setup and Running Tests

```bash
# install supported versions of python
pyenv install

# install packaging and build tools
pipx install tox
pipx install poetry

# install project dependencies
poetry install

# run all tests
tox run
```

### Testing

This project uses [pytest](https://docs.pytest.org/en/stable/) as the testing framework and [tox](https://github.com/tox-dev/tox)
as the test runner. testing. To run the tests, use the following commands:

```bash
# run all tests
tox run

# generate documentation
tox -e docs

# run specific tests with pytest directly using the default poetry environment
poetry run pytest tests -m "not integration" tests/models/requests/test_keyword_by_asins_request.py

# run integration tests using the default poetry environment
poetry run pytest tests -m "integration"
```

Note, running integration tests requires a `.env` file at the root of this project with real API keys.

```bash
# create a .env file from the template used for testing
cp .env.test .env
```

Then, add your real Jungle Scout API keys to the `.env` file:

```bash
API_KEY_NAME="real_api_key_name"
API_KEY="real_api_key"
```

### Code Formatting

This project uses [black](https://pypi.org/project/black/) for code formatting, [isort](https://pypi.org/project/isort/)
for import sorting and [ruff](https://github.com/astral-sh/ruff) as a linter. If you are using VSCode, you can
install the following extensions:

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
