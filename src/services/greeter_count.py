from src.repositories.greeting.type import GreetingRepo


class GreeterCountAppService:
    _repo: GreetingRepo

    def __init__(self, repo: GreetingRepo) -> None:
        self._repo = repo

    def run(self) -> int:
        return self._repo.count()
