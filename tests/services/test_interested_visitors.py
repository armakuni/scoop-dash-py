from src.repositories.visitors.in_memory import VisitorRepo
from src.services.visitors_service import InterestedVisitorsAppService


class TestInterestedVisitors:
    def test_initial_visitors_count(self) -> None:
        repo = VisitorRepo()
        interested_visitors = InterestedVisitorsAppService(repo)
        visitor_count = interested_visitors.get_visitors_count()
        assert visitor_count == 0

    def test_register_visitors_count(self) -> None:
        repo = VisitorRepo()
        interested_visitors = InterestedVisitorsAppService(repo)
        email = "john.doe@example.com"
        interested_visitors.register_visitor(email)
        assert repo.get_visitors_count() == 1
        visitor_count = interested_visitors.get_visitors_count()
        assert visitor_count == 1
