from src.repositories.visitors.in_memory import VisitorRepo


class InterestedVisitorsAppService:
    def __init__(self, data_store: VisitorRepo) -> None:
        self.data_store = data_store

    def get_visitors_count(self) -> int:
        return self.data_store.get_visitors_count()

    def register_visitor(self, email: str) -> None:
        self.data_store.register_visitor(email)
