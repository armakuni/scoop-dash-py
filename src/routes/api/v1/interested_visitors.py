import logging
from http import HTTPStatus

from flask import Blueprint, Response, jsonify

logger = logging.getLogger(__name__)
route = Blueprint("interested_visitors", __name__)


@route.route("/", methods=["GET"])
async def index() -> Response:
    # Like this but probably not in this file :-)
    # session = sessionmaker(engine, class_=Session, expire_on_commit=False)
    # with session() as s:
    #     result = s.execute(select(InterestedVisitor))
    #     logger.debug(result)

    return jsonify({"meta": {"count": 0}})


@route.route("/", methods=["POST"])
def create() -> tuple[Response, HTTPStatus]:
    return jsonify({"meta": {"count": 1}}), HTTPStatus.CREATED
