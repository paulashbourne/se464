from mongoengine import fields as f
from .base import BaseDocument

class Application(BaseDocument):
    job_id     = f.ObjectIdField()
    student_id = f.ObjectIdField()
