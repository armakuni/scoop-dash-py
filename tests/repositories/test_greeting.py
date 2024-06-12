from typing import Generator

import pytest
from assertpy import assert_that
from pytest import FixtureRequest
from sqlmodel import Session, select

from src.datastore import engine
from src.models.internal.greeting_incidenct import GreetingIncident
from src.repositories.greeting.in_memory import GreetingRepo as InMemoryGreetingRepo
from src.repositories.greeting.postgres import GreetingRepo as PostGresGreetingRepo


@pytest.fixture(params=["in_memory", "sql"])
def repository(
    request: FixtureRequest,
) -> Generator[InMemoryGreetingRepo | PostGresGreetingRepo, None, None]:
    if request.param == "in_memory":
        yield InMemoryGreetingRepo()
    else:
        with Session(engine) as session:
            clear_data(session)
            yield PostGresGreetingRepo(session)


def clear_data(session: Session) -> None:
    for incident in session.exec(select(GreetingIncident)):
        session.delete(incident)
    session.commit()
    session.expire_all()


class TestGreetingRepository:
    def test_it_should_give_me_a_counter_that_starts_at_0(
        self, repository: InMemoryGreetingRepo | PostGresGreetingRepo
    ) -> None:
        assert_that(repository.count()).is_equal_to(0)

    def test_it_should_allow_me_to_increment_it_2_times_and_show_me_the_count(
        self, repository: InMemoryGreetingRepo | PostGresGreetingRepo
    ) -> None:
        repository.increment()
        repository.increment()
        assert_that(repository.count()).is_equal_to(2)

    def test_it_should_allow_me_to_increment_it_3_times_and_show_me_the_count(
        self, repository: InMemoryGreetingRepo | PostGresGreetingRepo
    ) -> None:
        repository.increment()
        repository.increment()
        repository.increment()
        assert_that(repository.count()).is_equal_to(3)
