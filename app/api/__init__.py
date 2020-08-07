from flask_restful import Api
from .pin.routes import HashApi

hash_api = Api()


def create_module(app, **kwargs):
    hash_api.add_resource(HashApi, "/api/pin")
    hash_api.init_app(app)
