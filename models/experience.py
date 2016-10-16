from mongoengine import fields as f
from .base import BaseDocument

class Experience(BaseDocument):
    title      = f.StringField()
    company    = f.StringField()
    location   = f.StringField()

    start_time = f.DateTimeField()
    end_time   = f.DateTimeField()

    description = f.ListField(f.StringField())
