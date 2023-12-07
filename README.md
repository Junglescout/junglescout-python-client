# jungle-scout-python-client

Jungle Scout API Python Client.

## Installation

```bash
# install using Github personal access token for authentication
pip install git+https://${GITHUB_PERSONAL_TOKEN}@github.com/Junglescout/gong-client.git@main
```

## Development

### Running Tests

```bash
# install tox
pipx install tox

# install python versions for tox environments
pyenv install 3.7
pyenv install 3.8
pyenv install 3.9
pyenv install 3.10
pyenv install 3.11

# run quality tests against python versions
tox run
```

### Creating Local Development Environment

```bash
# its recommended to install the project in a virtual environment
# the example commands below use the `pyenv virtualenv` command to create the virtual environment
# see https://github.com/pyenv/pyenv-virtualenv for more information
pyenv virtualenv 3.7 jungle-scout-python-client-3.7
pyenv activate jungle-scout-python-client-3.7

# install project in editable mode with dev dependencies in the virtual environment
pip install -e .[dev]
```
