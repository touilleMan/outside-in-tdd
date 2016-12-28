
.PHONY: feature test

pyenv:
	pyenv install -s 3.4.5
	pyenv local 3.4.5

requirements:
	pip install -Ur requirements.txt

feature:
	pytest feature

test:
	pytest test

run:
	python -m app.application

