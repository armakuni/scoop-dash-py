tests:
	poetry run pytest tests

lint:
	poetry run ruff check
	poetry run mypy src tests

fmt:
	poetry run ruff format
	poetry run ruff lint --fix