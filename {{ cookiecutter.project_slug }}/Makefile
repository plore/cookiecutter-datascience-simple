.PHONY: init
init:
	poetry install --no-root

.PHONY: format
format:
	poetry run black .
	poetry run nbqa black .
	poetry run ruff check --select I --fix .
	find . -name "*.ipynb" -not -path "*ipynb_checkpoints*" -print0 | xargs -0 poetry run jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace

.PHONY: lint
lint:
	poetry run black --check .
	poetry run ruff .
