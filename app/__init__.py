from flask import Flask


def create_app(config_object):
    from app.api import create_module as api_create_module
    app = Flask(__name__)
    app.config.from_object(config_object)

    api_create_module(app)

    return app
