from mongoengine import fields as f
from .base import EmbeddedDocument

# A student's job experience
class Experience(EmbeddedDocument):
    title      = f.StringField(required = True)
    company    = f.StringField(required = True)
    location   = f.StringField()

    start_time = f.DateTimeField()
    end_time   = f.DateTimeField()

    description = f.StringField(default='')

    def to_dict(self):
        return {
            'title'       : self.title,
            'company'     : self.company,
            'location'    : self.location,
            'description' : self.description,
        }

