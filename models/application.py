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

    def to_dict(self):
        return {
            job_id     : str(self.job_id),
            student_id : str(self.student_id),
            state      : self.state
        }
    
    # To dict specifically for students
    def to_dict_student(self):
        _dict = self.to_dict()
        _dict.extend({
            'student_ranking' : student_ranking
        })
        return _dict
    
    # To dict specifically for students
    def to_dict_employer(self):
        _dict = self.to_dict()
        _dict.extend({
            'employer_ranking' : 'student_ranking'
        })
        return _dict
