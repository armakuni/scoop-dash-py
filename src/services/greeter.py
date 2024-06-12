from src.repositories.greeting.type import GreetingRepo


class GreeterAppService:
    _repo: GreetingRepo

    def __init__(self, repo: GreetingRepo):
        self._repo = repo

    def run(self) -> str:
        self._repo.increment()
        return "hello, world"
