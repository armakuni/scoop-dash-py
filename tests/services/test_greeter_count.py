import pytest
from assertpy import assert_that

from src.repositories.greeting.in_memory import GreetingRepo
from src.services.greeter_count import GreeterCountAppService


class TestGreeterCountAppService:
    @pytest.fixture
    def greeting_repo(self) -> GreetingRepo:
        return GreetingRepo()

    @pytest.fixture
    def app_service(self, greeting_repo: GreetingRepo) -> GreeterCountAppService:
        return GreeterCountAppService(greeting_repo)

    def test_it_returns_count_from_repo(
        self, app_service: GreeterCountAppService, greeting_repo: GreetingRepo
    ) -> None:
        greeting_repo.increment()
        greeting_repo.increment()
        greeting_repo.increment()
        assert_that(app_service.run()).is_equal_to(3)
