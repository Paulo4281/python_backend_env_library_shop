from src.routes.index_routes import book_routes
from src.utils.http_response import HttpResponse
from src.modules.book.controllers.book_controller import BookController
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required

@book_routes.route("/", methods=["POST"])
@jwt_required()
@cross_origin()
def save() -> HttpResponse:
    return BookController.save()

@book_routes.route("/", methods=["GET"])
@jwt_required()
@cross_origin()
def find() -> HttpResponse:
    return BookController.find()

@book_routes.route("/<id_>", methods=["GET"])
@jwt_required()
@cross_origin()
def find_by_id(id_: str) -> HttpResponse:
    return BookController.find_by_id(id_)

@book_routes.route("/<id_>", methods=["PUT"])
@jwt_required()
@cross_origin()
def update(id_: str) -> HttpResponse:
    return BookController.update(id_)

@book_routes.route("/<id_>", methods=["DELETE"])
@jwt_required()
@cross_origin()
def delete(id_: str) -> HttpResponse:
    return BookController.delete(id_)