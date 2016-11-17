from mongoengine import fields as f
from .base import BaseDocument
from models.experience import Experience
from models.education import Education
from models.user import User

class Student(User):
    meta = {
        'allow_inheritance' : False,
        'collection'        : 'student',
    }

    name = f.StringField(required = True)

    education  = f.EmbeddedDocumentListField(Education)
    experience = f.EmbeddedDocumentListField(Experience)

    # i.e. Python, Flask, React, etc.
    skills = f.ListField(f.StringField())

    def get_education(self):
        return map(lambda ed: ed.to_dict(), self.education)

    def get_experience(self):
        return map(lambda ex: ex.to_dict(), self.experience)

    def to_dict(self):
        return {
            'name': self.name,
            'education': self.get_education(),
            'experience': self.get_experience()
        }
