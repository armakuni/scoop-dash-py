
.PHONY: tests
tests:
	poetry run pytest tests

.PHONY: lint
lint:
	poetry run ruff check
	poetry run mypy src tests

.PHONY: fmt
fmt:
	poetry run ruff format
	poetry run ruff check --fix