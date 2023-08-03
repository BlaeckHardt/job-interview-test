from flask_restx import Api
from flask import Blueprint

from app.api.controller.entity import api as entity


blueprint = Blueprint("api", __name__, url_prefix="/v1")
authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(
    blueprint,
    title="FLASK RESTX API: DIVISIONAL DASHBOARD",
    version="1.0",
    description="A flask restx service for divisional information",
    authorizations=authorizations,
    security="apikey",
)

api.add_namespace(entity, path="/entity")
