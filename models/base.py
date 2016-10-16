from mongoengine import Document

class BaseDocument(Document):
    meta = {'allow_inheritance': True}

    @classmethod
    def create(cls, **kwargs):
        return cls(**kwargs)
