from mongoengine import fields as f
from .base import BaseDocument

class Education(BaseDocument):
    school     = f.StringField()
    degree     = f.StringField()
    start_time = f.DateTimeField()
    end_time   = f.DateTimeField()
