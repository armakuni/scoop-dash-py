import logging
from http import HTTPStatus
from typing import cast

from flask import Blueprint, Response, jsonify, request

from src.repositories.visitors.in_memory import VisitorRepo
from src.services.visitors_service import InterestedVisitorsAppService

logger = logging.getLogger(__name__)
route = Blueprint("interested_visitors", __name__)

vsisitor_repo = VisitorRepo()


@route.route("/", methods=["GET"])
async def index() -> Response:
    # Like this but probably not in this file :-)
    # session = sessionmaker(engine, class_=Session, expire_on_commit=False)
    # with session() as s:
    #     result = s.execute(select(InterestedVisitor))
    #     logger.debug(result)
    visitors_service = InterestedVisitorsAppService(vsisitor_repo)
    visitors_count = visitors_service.get_visitors_count()
    return jsonify({"meta": {"count": visitors_count}})


@route.route("/", methods=["POST"])
def create() -> tuple[Response, HTTPStatus]:
    email = cast(str, request.json)
    visitors_service = InterestedVisitorsAppService(vsisitor_repo)
    visitors_service.register_visitor(email)
    visitors_count = visitors_service.get_visitors_count()
    return jsonify({"meta": {"count": visitors_count}}), HTTPStatus.CREATED
