import pytest
from assertpy import assert_that
from httpx import URL, Client
from sqlmodel import Session, select

from src.datastore import engine
from src.models.internal.greeting_incidenct import GreetingIncident


class TestHello:
    @pytest.fixture(autouse=True)
    def clear_data(self) -> None:
        with Session(engine) as session:
            for incident in session.exec(select(GreetingIncident)):
                session.delete(incident)
            session.commit()
            session.expire_all()

    def test_hello(self, client: Client, base_url: URL) -> None:
        response = client.get(f"{base_url}/hello/")
        assert_that(response).has_status_code(200)
        assert_that(response).has_text("hello, world")

    def test_hello_counts_the_number_of_times_called(
        self, client: Client, base_url: URL
    ) -> None:
        client.get(f"{base_url}/hello/")
        client.get(f"{base_url}/hello/")
        client.get(f"{base_url}/hello/")

        response = client.get(f"{base_url}/hello/count/")
        assert_that(response).has_status_code(200)
        assert_that(response).has_text("3")
