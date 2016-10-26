class BaseConfig(object):
    # General
    DEBUG       = False
    TESTING     = False

    # Database
    DB_NAME     = None
    DB_HOST     = None
    DB_USER     = None
    DB_PASSWORD = None
    DB_PORT     = None

class DevelopmentConfig(BaseConfig):
    # General
    DEBUG   = True

    # Database
    DB_NAME = 'WaterlooActuallyWorks_development'
    DB_HOST = 'localhost'

class TestingConfig(BaseConfig):
    # General
    TESTING = True

    # Database
    DB_NAME = 'WaterlooActuallyWorks_testing'
    DB_HOST = 'localhost'

def get_config(env):
    from app import Environment

    if env == Environment.DEVELOPMENT:
        return DevelopmentConfig
    elif env == Environment.TESTING:
        return TestingConfig
    else:
        raise Exception("Unrecognized config environment")
