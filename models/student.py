from mongoengine import fields as f
from .base import BaseDocument

class Student(BaseDocument):
    name = f.StringField(required = True)

    # List of Education.id's
    education  = f.ListField(f.ObjectIdField())

    # i.e. Python, Flask, React, etc.
    skills = f.ListField(f.StringField())

    @classmethod
    def dict_include(cls):
        return [
            'id',
            'name',
            'education',
            'skills',
        ]
