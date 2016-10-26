from mongoengine import fields as f
from .base import BaseDocument

class Student(BaseDocument):
    name = f.StringField()

    # List of Education.id's
    education  = f.ListField(f.ObjectIdField())

    # i.e. Python, Flask, React, etc.
    skills = f.ListField(f.StringField())

    @classmethod
    def dict_include(cls):
        return [
            'name'
        ]
