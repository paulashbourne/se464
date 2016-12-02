import os

# Base configuration
# Default values for all options
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

class ProductionConfig(BaseConfig):
    # Database
    DB_NAME = 'WaterlooActuallyWorks_production'
    DB_HOST = os.environ.get('MONGODB_URI')

# Get configuration object associated with given app environment
def get_config(env):
    from app import Environment

    if env == Environment.DEVELOPMENT:
        return DevelopmentConfig
    elif env == Environment.TESTING:
        return TestingConfig
    elif env == Environment.PRODUCTION:
        return ProductionConfig
    else:
        raise Exception("Unrecognized config environment")
