from mongoengine import fields as f
from .base import BaseDocument
import bcrypt

class User(BaseDocument):
    meta = {
        'abstract': True
    }

    email = f.StringField(required = True, unique = True)

    password = f.StringField(required = True)

    @classmethod
    def encrypt_password(cls, password):
        return bcrypt.hashpw(password, bcrypt.gensalt())
