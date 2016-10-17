import mongoengine

def connect_db():
    mongoengine.connect('localhost')
