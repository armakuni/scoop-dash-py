import httpx


def test_hello(client: httpx.Client, base_url: httpx.URL) -> None:
    response = client.get(f"{base_url}/hello")
    assert response.status_code == 200
    assert response.text == "hello, world"
