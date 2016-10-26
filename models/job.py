from mongoengine import fields as f
from .base import BaseDocument
from models import Employer

class Job(BaseDocument):
    meta = {'collection': 'jobs'}

    employer_id = f.ObjectIdField()
    position    = f.StringField()
    description = f.StringField()
    location    = f.StringField()
    openings    = f.IntField()

    def to_dict(self):
        employer = Employer.by_id(self.employer_id)
        return {
            'company_name': employer.company_name,
            'employer_id': str(self.employer_id),
            'position': self.position,
            'description': self.description,
            'location': self.location,
            'openings': self.openings
        }
