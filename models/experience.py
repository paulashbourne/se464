from mongoengine import fields as f
from .base import BaseDocument

class Experience(BaseDocument):
    meta = {
        'allow_inheritance' : False,
        'collection'        : 'experience',
    }

    student_id = f.ObjectIdField(required = True)

    title      = f.StringField(required = True)
    company    = f.StringField(required = True)
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
