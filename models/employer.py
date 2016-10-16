from mongoengine import fields as f
from .base import BaseDocument

class Employer(BaseDocument):
    company_name = f.StringField()
    website      = f.StringField()
    # List of recruiter emails
    emails       = f.ListField(f.StringField())
