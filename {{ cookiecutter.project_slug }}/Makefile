.PHONY: init
init:
	pipenv lock
	pipenv sync --dev
	pipenv run jupyter contrib nbextension install --sys-prefix