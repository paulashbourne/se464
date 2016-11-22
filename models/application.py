from mongoengine import fields as f
from .base import BaseDocument
from student import Student
from job import Job

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
        student = Student.objects(id=self.student_id)[0]
        job = Job.objects(id=self.job_id)[0]
        return {
            'id': str(self.id),
            'job_id': str(self.job_id),
            'job': job.to_dict(),
            'student_id': str(self.student_id),
            'student_name': student.name,
            'student_ranking': self.student_ranking,
            'employer_ranking': self.employer_ranking
        }

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
