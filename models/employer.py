from mongoengine import fields as f
from .base import BaseDocument

class Employer(BaseDocument):
    meta = {
        'allow_inheritance' : False,
        'collection'        : 'employer',
    }


    company_name = f.StringField(required = True, unique = True)
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
