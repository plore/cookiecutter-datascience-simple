.PHONY: init
init:
	pipenv lock
	pipenv sync --dev
	pipenv run jupyter contrib nbextension install --sys-prefix

.PHONY: format
format:
	pipenv run black .
	pipenv run isort .
	find -name "*.ipynb" -not -path "*ipynb_checkpoints*" -print0 | xargs -0 pipenv run jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace

.PHONY: lint
lint:
	pipenv run black --check .
	pipenv run isort --check .
	pipenv run flake8 .