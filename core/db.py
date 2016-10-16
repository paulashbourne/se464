import constants
import mongoengine

def connect_db():
    mongoengine.connect(constants.DB_NAME)
