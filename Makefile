.PHONY: init
init:
	poetry install

.PHONY: test
test:
	poetry run pytest -s -k "not initialization"

.PHONY: test-all
test-all:
	poetry run pytest -s

.PHONY: format
format:
	poetry run black .
	poetry run isort .

.PHONY: lint
lint:
	poetry run black --check .
	poetry run isort --check .
	poetry run flake8 .
	poetry run pylint .
