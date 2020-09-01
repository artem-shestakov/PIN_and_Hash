from flask import Flask


# create Flask app object and init all modules
def create_app(config_object):
    from .main import create_module as main_create_module
    from app.api import create_module as api_create_module

    # Init APP
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Init modules
    main_create_module(app)
    app.logger.info("Init Main module")

    api_create_module(app)
    app.logger.info("Init API module")

    return app
