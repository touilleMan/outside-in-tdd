
.PHONY: test
.DEFAULT_GOAL := test-all

pyenv:
	pyenv install -s 3.4.5
	pyenv local 3.4.5

requirements:
	pip install -Ur requirements.txt

test-feature:
	pytest feature

test:
	pytest test

test-all:
	pytest test feature

run:
	python -m app.application

clean:
	find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -delete

