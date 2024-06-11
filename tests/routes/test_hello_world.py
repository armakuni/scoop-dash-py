from assertpy import assert_that
from flask.testing import FlaskClient


def test_request_example(client: FlaskClient) -> None:
    response = client.get("/hello/")
    assert_that(response).has_status_code(200)
    assert_that(response).has_text("hello, world")
