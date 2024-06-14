from unittest import mock

from assertpy import assert_that
from flask.testing import FlaskClient

from src.services.visitors_service import InterestedVisitorsAppService


class TestInterestedVisitors:
    def test_should_start_at_zero(self, client: FlaskClient) -> None:
        with mock.patch.object(
            InterestedVisitorsAppService, "get_visitors_count"
        ) as visitors_app:
            visitors_app.return_value = 0
            response = client.get("/api/v1/interested-visitors/")
            assert_that(response).has_status_code(200)
            assert_that(response).has_json({"meta": {"count": 0}})

    def test_get_interested_visitors_count(self, client: FlaskClient) -> None:
        with mock.patch.object(
            InterestedVisitorsAppService, "get_visitors_count"
        ) as visitors_app:
            visitors_app.return_value = 1
            response = client.get("/api/v1/interested-visitors/")
            assert_that(response).has_status_code(200)
            assert_that(response).has_json({"meta": {"count": 1}})

    # @patch("services.visitors_service.InterestedVisitorsAppService")
    # def test_should_return_number_visitors(
    #     self, client: FlaskClient, mock_service: InterestedVisitorsAppService
    # ) -> None:
    #     visitors_count = mock_service.get_visitors_count()
    # visitors_count
    # response = client.post("/api/v1/interested-visitors/")
    # assert_that(response).has_status_code(200)
    # assert_that(response).has_json({"meta": {"count": 0}})
