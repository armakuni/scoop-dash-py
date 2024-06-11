from assertpy import assert_that
from flask.testing import FlaskClient


class TestInterestedVisitors:
    def test_should_start_at_zero(self, client: FlaskClient) -> None:
        response = client.get("/api/v1/interested-visitors/")
        assert_that(response).has_status_code(200)
        assert_that(response).has_json({"meta": {"count": 0}})
