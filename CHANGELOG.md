# CHANGELOG



## v1.0.0 (2024-03-18)

### Breaking

* feat: migrate to pydantic and add additional linting tests (#42)

BREAKING CHANGE: `response` objects have changed from native `dict` objects to `pydantic.BaseModel` objects ([`d412e10`](https://github.com/Junglescout/jungle-scout-python-client/commit/d412e10450971a9f553fe8539ebcf2e0797b59dc))

### Documentation

* docs: cleanup docs (#41) ([`51a4d6d`](https://github.com/Junglescout/jungle-scout-python-client/commit/51a4d6de4f1257615431cc31aa60d61d4884f601))

* docs: Add basic Documentation (#40) ([`aed6498`](https://github.com/Junglescout/jungle-scout-python-client/commit/aed6498050861133594bc9e733ca4b58a683e5b3))

### Test

* test: Add Final Integrity tests (#39) ([`e51f2f6`](https://github.com/Junglescout/jungle-scout-python-client/commit/e51f2f6abb9afcb9bbab8a9bdc99736c4bdd8938))


## v0.1.0 (2024-03-14)

### Feature

* feat: adds semantic versioning, build step, and publishing step (#34) ([`5b02132`](https://github.com/Junglescout/jungle-scout-python-client/commit/5b021327ef985a51786e349bf051abd7008df61b))

### Unknown

* Updates Contributions README and Removing unused dependencies (#32)

* fail docs

* add build step for docs

* updates

* updates

* updates

* desc

* remove examples

* format ([`1232110`](https://github.com/Junglescout/jungle-scout-python-client/commit/1232110c2fd66d5109f5fc6ffb4bcfab4215d3be))

* Add MIT License to the project (#33) ([`ed7024e`](https://github.com/Junglescout/jungle-scout-python-client/commit/ed7024e677ba30319c95f1983a04bbfd04552dfe))

* Use full location to poetry (#31) ([`c2f8f75`](https://github.com/Junglescout/jungle-scout-python-client/commit/c2f8f750c4da2b5ed5de91ec07b0462d6be19832))

* Change how poetry is installed (#30) ([`40ebbce`](https://github.com/Junglescout/jungle-scout-python-client/commit/40ebbce94c4701e9d1899b446ef257701123d29f))

* Add .readthedocs.yaml configuration file (#29) ([`35e494b`](https://github.com/Junglescout/jungle-scout-python-client/commit/35e494bac77f089a5e5cf9b212cf6a5abf001ecc))

* Setup Docs with sphinx  (#28)

* install sphinx

* initial commit of docs

* add new theme

* remove makefile

* create the docs

* updates

* newline ([`0583173`](https://github.com/Junglescout/jungle-scout-python-client/commit/0583173c3d71fa921a8f099a385d4cbc63d9ea03))

* Add Click and Conversions example (#27) ([`e9a0c7c`](https://github.com/Junglescout/jungle-scout-python-client/commit/e9a0c7caeecbf46c097dbce8f4db7c278c416f8d))

* Add readme and contributing sections (#25)

* Add readme and contributing

* Removes test file

* Fix lint and add ruff to the readme

* Lint errors ([`45d9337`](https://github.com/Junglescout/jungle-scout-python-client/commit/45d9337ccb5dbb4b34d30bae70bde1e97de1962d))

* WIP: Refactor requests (#24)

* Update the keywords-by-keyword methods and wire some tests

* Lint issues

* Convert historical search and keywords_by asin to new format

* Refactor sales_estimates

* Sales_estimates

* Refactor share of voice

* Refactor product database

* Add some to-dos

* Disable integration tests temporarily

* Re-enable integration tests

* Fix tests

* Add a todo ([`3376377`](https://github.com/Junglescout/jungle-scout-python-client/commit/33763773a47a576a78ce2f5cd38ad14511e5b389))

* Add patterns for testing (#22)

* adds a custom marker for integration tests

* better test

* move

* generate test

* better import

* fix

* fixes

* fix types

* fix sort ([`3277eee`](https://github.com/Junglescout/jungle-scout-python-client/commit/3277eee8c4b2ef39d51aed3983a60895a379f622))

* Add ruff to CI (#21) ([`69b66d0`](https://github.com/Junglescout/jungle-scout-python-client/commit/69b66d075253bee810624407e611d460e72f499a))

* Move Base Request into requests package (#20)

* move base request

* fix ([`7d102a3`](https://github.com/Junglescout/jungle-scout-python-client/commit/7d102a3526db44aa903ebc1fb0c028b3a0c624a2))

* Export &#34;public&#34; classes from __init__.py files (#19)

* move responses and parameters

* fix imports

* resolve circular import ([`2aad359`](https://github.com/Junglescout/jungle-scout-python-client/commit/2aad359bdd2b4f7771ec87ff608701f2e86a9b1f))

* Adds SOV and Product DB requests (#18)

* Add models and basic request

* Add product_database request ([`66045de`](https://github.com/Junglescout/jungle-scout-python-client/commit/66045de090f79eb2301e4ee35ca66f235d1c0cd9))

* Add historical_search_volume and sales_estimates request (#15)

* Lint and isort

* Update README with black and isort

* WIP: historical search volume request

* Adds sales_estimate and historical_search requests

* Minor Improvements

* Update request classes ([`2ee393d`](https://github.com/Junglescout/jungle-scout-python-client/commit/2ee393ddb89a7859a8c42682ac06f36cdbaf8077))

* Specify the `pythonpath` why running `pyright` (#16)

* fix

* debug

* remove from pyproject.toml ([`6b99647`](https://github.com/Junglescout/jungle-scout-python-client/commit/6b99647d923327fe44a71ff7ff58b02e0bae61f2))

* Install pyright and run during CI (#14)

* install pyright and run during ci

* use abstract properties

* black and isort

* fix type issues

* fix type issues

* fix enum

* fix

* fix

* typeright requires node

* local .venv

* use poetry to run pyright ([`7c82334`](https://github.com/Junglescout/jungle-scout-python-client/commit/7c82334ac174d6d49e858ae284803b1f52a6aa7c))

* Adds keywords_* models (#4)

* Adds keyword by asin request model

* WIP: Refactoring keywrods_by_keywords request

* Adds keywords_by_keyword request functions

* Keywords by ASIN Request (#5)

* isort and black

* delete about

* udpates!

* add todos

* fix sorting

* Update readme

* update

* updates

* Added Enums and fixed keywords_by_keyword call

---------

Co-authored-by: Salim &lt;salim@junglescout.com&gt; ([`3d30b0c`](https://github.com/Junglescout/jungle-scout-python-client/commit/3d30b0ce83c615049b383dbd48d500931268ea84))

* Migrate to poetry and add CI checks (#3)

* migrate to poetry

* Add CI workflow configuration for poetry and tox

* run on linux

* drop support for python 3.8. Add support for python 3.12

* updates

* more udpates ([`6ef53f9`](https://github.com/Junglescout/jungle-scout-python-client/commit/6ef53f9a96203ebacf1dda3b6929e1663745bb8c))

* WIP: Add new endpoint ([`812e231`](https://github.com/Junglescout/jungle-scout-python-client/commit/812e23176bd0707e710ef45deda1a46f1b1a5c90))

* Update README.md install directions (#2) ([`04eda0a`](https://github.com/Junglescout/jungle-scout-python-client/commit/04eda0a2011701191522a6af3459efa6ba5be3a5))

* Setup project and add a simple API endpoints as an example (#1)

* add ignore

* projects setup

* ability to run tests

* fix tests

* translate to model

* fix readme ([`4a493bb`](https://github.com/Junglescout/jungle-scout-python-client/commit/4a493bb673b57d4955c87a04b7bd3b2c28fa86f7))

* first commit ([`40b03c9`](https://github.com/Junglescout/jungle-scout-python-client/commit/40b03c9dc7be24d5c356d4d731db6638c6073359))
