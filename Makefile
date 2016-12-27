
.PHONY: feature test

feature: test
	pytest feature

test:
	pytest test

