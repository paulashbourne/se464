from mongoengine import fields as f
from .base import BaseDocument

class Employer(BaseDocument):
    meta = {'collection': 'employers'}

    company_name = f.StringField(unique=True)
    website      = f.StringField()
    # List of recruiter emails
    emails       = f.ListField(f.StringField())

    @classmethod
    def dict_include(self):
        return [
            'id',
            'company_name',
            'website',
            'emails'
        ]
