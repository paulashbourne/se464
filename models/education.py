from mongoengine import fields as f
from .base import BaseDocument

class Education(BaseDocument):
    school     = f.StringField()
    degree     = f.StringField()
    major      = f.StringField()
    start_time = f.DateTimeField()
    end_time   = f.DateTimeField()

    @classmethod
    def dict_include(cls):
        return [
            'id',
            'school',
            'degree',
            'major',
            'start_time',
            'end_time'
        ]
