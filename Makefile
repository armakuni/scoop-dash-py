
.PHONY: tests
tests:
	poetry run pytest tests

.PHONY: e2e
e2e:
	poetry run pytest e2e


.PHONY: lint
lint:
	poetry run ruff check
	poetry run mypy src tests e2e

.PHONY: fmt
fmt:
	poetry run ruff format
	poetry run ruff check --fix