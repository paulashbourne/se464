from mongoengine import fields as f
from .base import BaseDocument

class User(BaseDocument):
    meta = {
        'abstract': True
    }

    email = f.StringField(required = True, unique = True)

    password = f.StringField(required = True)
