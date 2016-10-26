from mongoengine import fields as f
from .base import BaseDocument

class Application(BaseDocument):
    job_id     = f.ObjectIdField(required = True)
    student_id = f.ObjectIdField(required = True)

    # Fields which should be returned in a to_dict
    @classmethod
    def dict_include(self):
        return [
            'id',
            'job_id',
            'student_id'
        ]
