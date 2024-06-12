from flask import Blueprint
from sqlmodel import Session

from src.datastore import engine
from src.repositories.greeting.postgres import GreetingRepo
from src.services.greeter import GreeterAppService
from src.services.greeter_count import GreeterCountAppService

route = Blueprint("hello", __name__)


@route.route("/", methods=["GET"])
def hello_world() -> str:
    with Session(engine) as session:
        service = GreeterAppService(GreetingRepo(session))
        return service.run()


@route.route("/count/", methods=["GET"])
def count() -> str:
    with Session(engine) as session:
        service = GreeterCountAppService(GreetingRepo(session))
        return str(service.run())
