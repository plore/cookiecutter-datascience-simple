.PHONY: init
init:
	poetry install
	poetry run jupyter contrib nbextension install --sys-prefix

.PHONY: format
format:
	poetry run black .
	poetry run isort .
	find -name "*.ipynb" -not -path "*ipynb_checkpoints*" -print0 | xargs -0 pipenv run jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace

.PHONY: lint
lint:
	poetry run black --check .
	poetry run isort --check .
	poetry run flake8 .