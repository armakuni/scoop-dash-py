import os

from flask import Flask

from src.routes import hello_world
from src.routes.api.v1 import interested_visitors


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(
        blueprint=interested_visitors.route, url_prefix="/api/v1/interested-visitors"
    )
    app.register_blueprint(blueprint=hello_world.route, url_prefix="/hello/")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        debug=True,
        host="::",
        port=int(os.environ["PORT"]) if "PORT" in os.environ else None,
    )
