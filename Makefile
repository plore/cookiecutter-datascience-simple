.PHONY: init
init:
	poetry install --no-root

.PHONY: test
test:
	poetry run pytest -s -k "not initialization"

.PHONY: test-all
test-all:
	poetry run pytest -s -k "not initialization"
	poetry run pytest -k "initialization"

.PHONY: format
format:
	poetry run black .
	poetry run ruff check --select I --fix .

.PHONY: lint
lint:
	poetry run black --check .
	poetry run ruff .
	poetry run pylint .
