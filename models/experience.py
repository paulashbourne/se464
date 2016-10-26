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
