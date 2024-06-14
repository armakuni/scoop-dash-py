class VisitorRepo:
    _visitors: set[str]

    def __init__(self) -> None:
        self._visitors = set()

    def get_visitors_count(self) -> int:
        return len(self._visitors)

    def register_visitor(self, email: str) -> None:
        self._visitors.add(email)
