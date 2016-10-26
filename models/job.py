from mongoengine import fields as f
from .base import BaseDocument
from models import Employer

class Job(BaseDocument):
    meta = {
        'allow_inheritance' : False,
        'collection'        : 'job',
    }

    employer_id = f.ObjectIdField(required = True)
    position    = f.StringField(required = True)
    description = f.StringField(required = True)
    location    = f.StringField(required = True)
    openings    = f.IntField()

    def to_dict(self):
        employer = Employer.by_id(self.employer_id)
        return {
            'job_id': str(self.id),
            'company_name': employer.company_name,
            'employer_id': str(self.employer_id),
            'position': self.position,
            'description': self.description,
            'location': self.location,
            'openings': self.openings
        }
