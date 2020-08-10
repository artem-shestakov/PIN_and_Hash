from flask import Flask
from logging import StreamHandler, INFO
import sys, logging


# create Flask app object and init all modules
def create_app(config_object):
    from .main import create_module as main_create_module
    from app.api import create_module as api_create_module

    # Init APP
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Init app logger
    # logger = logging.getLogger()
    # logger.setLevel(logging.INFO)
    #
    # stdout_log = StreamHandler(stream=sys.stdout)
    # stdout_log.setLevel(INFO)
    #
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # stdout_log.setFormatter(formatter)
    # app.logger.addHandler(stdout_log)

    # Init modules
    main_create_module(app)
    app.logger.info("Init Main module")
    api_create_module(app)
    app.logger.info("Init API module")

    return app
