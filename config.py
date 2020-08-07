class Config(object):
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
    PREFERRED_URL_SCHEME = "https"


