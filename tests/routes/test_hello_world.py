from unittest import mock

from assertpy import assert_that
from flask.testing import FlaskClient

from src.services.greeter import GreeterAppService
from src.services.greeter_count import GreeterCountAppService


class TestHelloWorldRoute:
    def test_get_example(self, client: FlaskClient) -> None:
        with mock.patch.object(GreeterAppService, "run") as hello_world_app:
            hello_world_app.return_value = "hello, world"
            response = client.get("/hello/")
            assert_that(response).has_status_code(200)
            assert_that(response).has_text("hello, world")

    def test_get_count_example(self, client: FlaskClient) -> None:
        with mock.patch.object(GreeterCountAppService, "run") as hello_world_app:
            hello_world_app.return_value = "0"
            response = client.get("/hello/count/")
            assert_that(response).has_status_code(200)
            assert_that(response).has_text("0")
