from assertpy import assert_that
from httpx import URL, Client


class TestInterestedVisitorCount:
    def test_it_should_let_me_register_an_email(
        self, client: Client, base_url: URL
    ) -> None:
        client.get(f"{base_url}/api/v1/interested-visitors/")
        response = client.post(
            f"{base_url}/api/v1/interested-visitors/", json="an-email@example.com"
        )

        assert_that(response).has_status_code(201)
        assert_that(response.json()).is_equal_to({"meta": {"count": 1}})

    def test_it_should_maintain_the_count_between_requests(
        self, client: Client, base_url: URL
    ) -> None:
        client.get(f"{base_url}/api/v1/interested-visitors/")
        client.post(
            f"{base_url}/api/v1/interested-visitors/", json="an-email@example.com"
        )
        response = client.get(f"{base_url}/api/v1/interested-visitors/")

        assert_that(response).has_status_code(200)
        assert_that(response.json()).is_equal_to({"meta": {"count": 1}})
