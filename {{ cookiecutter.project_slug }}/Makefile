.PHONY: init
init:
	pipenv lock
	pipenv sync --dev
	pipenv run jupyter contrib nbextension install --sys-prefix

.PHONY: format
format:
	pipenv run black .
	pipenv run isort .

.PHONY: lint
lint:
	pipenv run black --check .
	pipenv run isort --check .
	pipenv run flake8 .