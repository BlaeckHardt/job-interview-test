import flask
import logging

from flask import Flask
from flask_cors import CORS

from app.api import blueprint as apiv1
from app.config import config_by_name


logging.basicConfig(
    format="%(asctime)s || %(name)s || %(levelname)s || %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(apiv1)
    app.app_context().push()
    CORS(app)

    return app
