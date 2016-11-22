from mongoengine import fields as f
from .base import BaseDocument
from models import Employer
from models import Application

class Job(BaseDocument):
    meta = {
        'allow_inheritance' : False,
        'collection'        : 'job',
    }

    class State():
        OPEN             = "OPEN"
        CANCELLED        = "CANCELLED"
        FILLED           = "FILLED"
        UNFILLED         = "UNFILLED"
        PARTIALLY_FILLED = "PARTIALLY_FILLED"

    employer_id = f.ObjectIdField(required = True)
    position    = f.StringField(required = True)
    description = f.StringField(required = True)
    location    = f.StringField(required = True)
    openings    = f.IntField()
    state       = f.StringField(required = True, default = State.OPEN)

    def to_dict(self):
        _dict = {
            'job_id'       : str(self.id),
            'employer_id'  : str(self.employer_id),
            'position'     : self.position,
            'description'  : self.description,
            'location'     : self.location,
            'openings'     : self.openings,
            'applications' : map(lambda app: app.to_dict(), Application.objects(job_id=self.id))
        }
        employer = Employer.by_id(self.employer_id)
        if employer:
            _dict.update({
                'company_name' : employer.company_name
            })
        return _dict
