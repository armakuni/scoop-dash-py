from flask import Blueprint

route = Blueprint("hello", __name__)


@route.route("/")
def hello_world() -> str:
    return "hello, world"
