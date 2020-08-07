from flask import Flask


# create Flask app object and init all modules
def create_app(config_object):
    from .main import create_module as main_create_module
    from app.api import create_module as api_create_module
    app = Flask(__name__)
    app.config.from_object(config_object)

    main_create_module(app)
    api_create_module(app)

    return app
