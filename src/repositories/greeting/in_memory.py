class GreetingRepo:
    def __init__(self) -> None:
        self._count = 0

    def count(self) -> int:
        return self._count

    def increment(self) -> None:
        self._count = self._count + 1
