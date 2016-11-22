from mongoengine import fields as f
from .base import BaseDocument
from models.student import Student

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
        student = Student.by_id(self.student_id)
        _dict = {
            'id'               : str(self.id),
            'job_id'           : str(self.job_id),
            'student_id'       : str(self.student_id),
            'student_ranking'  : self.student_ranking,
            'employer_ranking' : self.employer_ranking,
            'state'            : self.state
        }
        if student:
            _dict.update({
                'student_name' : student.name,
            })
        return _dict

    # To dict specifically for students
    def to_dict_student(self):
        _dict = self.to_dict()
        _dict.update({
            'student_ranking' : self.student_ranking
        })
        return _dict

    # To dict specifically for students
    def to_dict_employer(self):
        _dict = self.to_dict()
        _dict.update({
            'employer_ranking' : self.student_ranking
        })
        return _dict
