from mongoengine import fields as f
from .base import BaseDocument

class Experience(BaseDocument):
    student_id = f.ObjectIdField()

    title      = f.StringField()
    company    = f.StringField()
    location   = f.StringField()

    start_time = f.DateTimeField()
    end_time   = f.DateTimeField()

    description = f.StringField()

    @classmethod
    def dict_include(cls):
        return [
            'id',
            'student_id',
            'title',
            'company',
            'location',
            'start_time',
            'end_time',
            'description'
        ]
