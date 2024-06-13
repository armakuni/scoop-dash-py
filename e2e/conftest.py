import os
import time
from subprocess import Popen
from typing import Generator

import pytest
from httpx import URL, Client, ConnectError

PORT = "5002"


@pytest.fixture()
def server(base_url: URL) -> Generator[Popen[bytes], None, None]:
    import subprocess

    process = subprocess.Popen(
        [
            "poetry",
            "run",
            "flask",
            "--app",
            "scoop_dash_py:create_app()",
            "run",
            "--port",
            PORT,
        ],
        env=dict(os.environ),
    )

    while True:
        try:
            if Client().get(base_url):
                break
        except ConnectError:
            time.sleep(1)

    yield process
    process.terminate()
    process.wait()


@pytest.fixture()
def client(server: Popen[bytes]) -> Generator[Client, None, None]:
    with Client() as client:
        yield client


@pytest.fixture()
def base_url() -> URL:
    return URL(f"http://localhost:{PORT}")
