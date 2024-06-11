from assertpy import assert_that
from httpx import URL, Client


def test_hello(client: Client, base_url: URL) -> None:
    response = client.get(f"{base_url}/hello/")
    assert_that(response).has_status_code(200)
    assert_that(response).has_text("hello, world")
