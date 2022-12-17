.PHONY: init
init:
	pipenv lock
	pipenv sync --dev

.PHONY: test
test:
	pipenv run pytest -s -k "not initialization"

.PHONY: test-all
test-all:
	pipenv run pytest -s

.PHONY: format
format:
	pipenv run black .
	pipenv run isort .

.PHONY: lint
lint:
	pipenv run black --check .
	pipenv run isort --check .
	pipenv run flake8 .
	pipenv run pylint .
