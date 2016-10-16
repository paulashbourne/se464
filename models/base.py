from mongoengine import Document

class BaseDocument(Document):
    meta = {'allow_inheritance': True}
