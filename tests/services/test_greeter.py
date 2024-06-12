import pytest
from assertpy import assert_that

from src.repositories.greeting.in_memory import GreetingRepo
from src.services.greeter import GreeterAppService


class TestGreeterAppService:
    @pytest.fixture
    def greeting_repo(self) -> GreetingRepo:
        return GreetingRepo()

    @pytest.fixture
    def app_service(self, greeting_repo: GreetingRepo) -> GreeterAppService:
        return GreeterAppService(greeting_repo)

    def test_it_returns_hello_world(self, app_service: GreeterAppService) -> None:
        assert_that(app_service.run()).is_equal_to("hello, world")

    def test_it_increments_the_greeting_count(
        self, app_service: GreeterAppService, greeting_repo: GreetingRepo
    ) -> None:
        app_service.run()
        assert_that(greeting_repo.count()).is_equal_to(1)
