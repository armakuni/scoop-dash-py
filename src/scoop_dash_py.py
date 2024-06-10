from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello_world() -> str:
    return "hello, world"
