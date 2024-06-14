# import pytest
# from pytest import FixtureRequest
# from sqlmodel import Session, select

# from src.models.internal.greeting_incidenct import GreetingIncident
from src.repositories.visitors.in_memory import VisitorRepo as InMemoryVisitorRepo

# from src.repositories.greeting.postgres import GreetingRepo as PostGresGreetingRepo


# @pytest.fixture(params=["in_memory"])
def test_repository() -> None:
    assert InMemoryVisitorRepo() is not None


def test_repository_get_visitors_count() -> None:
    repo = InMemoryVisitorRepo()
    visitors_count = repo.get_visitors_count()
    assert visitors_count == 0


def test_repository_register_visitors() -> None:
    repo = InMemoryVisitorRepo()
    email = "john.doe@example.com"
    repo.register_visitor(email)
    visitors_count = repo.get_visitors_count()
    assert visitors_count == 1
