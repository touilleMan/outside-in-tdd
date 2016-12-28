
.PHONY: feature test

feature:
	pytest feature

test:
	pytest test

run:
	python -m app.application

