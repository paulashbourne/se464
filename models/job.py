from mongoengine import fields as f
from .base import BaseDocument

class Job(BaseDocument):
    employer_id = f.ObjectIdField()
    position    = f.StringField()
    description = f.StringField()
    location    = f.StringField()
    openings    = f.IntField()

    @classmethod
    def dict_include(cls):
        return [
            'id',
            'employer_id',
            'position',
            'description',
            'location',
            'openings',
        ]
