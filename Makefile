.DEFAULT_GOAL := tests

clean:
	git clean -Xdf
	rm -rf build/ dist/

tests:
	tox

test-deps:
	pip install -e .[dev]
