class Config(object):
    POSTS_PER_PAGE = 10
    PREFERRED_URL_SCHEME = "https"


class ProdConfig(Config):
    DEBUG = False
    ENV = "production"


class DevConfig(Config):
    DEBUG = True

