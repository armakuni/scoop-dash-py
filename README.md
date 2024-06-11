# ScoopDash

Run unit tests

``` shell
    poetry run pytest tests
```

Run end to end tests

``` shell
    poetry run pytest e2e
```

Check formatting and linting

``` shell
    poetry run ruff check
    poetry run mypy src tests e2e
```

Format and fix failing lints as possible

``` shell
    poetry run ruff format
    poetry run ruff check --fix
```
