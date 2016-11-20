from mongoengine import fields as f
from .base import BaseDocument

class Application(BaseDocument):
    meta = {
        'allow_inheritance' : False,
        'collection'        : 'application',
    }

    class State():
        APPLIED     = "APPLIED"
        MATCHED     = "MATCHED"
        NOT_MATCHED = "NOT_MATCHED"

    job_id           = f.ObjectIdField(required = True)
    student_id       = f.ObjectIdField(required = True)
    state            = f.StringField(required = True, default = State.APPLIED)
    student_ranking  = f.IntField(required = False, min_value = 1)
    employer_ranking = f.IntField(required = False, min_value = 1)

    # Fields which should be returned in a to_dict
    @classmethod
    def dict_include(self):
        return [
            'id',
            'job_id',
            'student_id'
        ]
