from mongoengine import fields as f
from .base import EmbeddedDocument

class Education(EmbeddedDocument):
    meta = {
        'allow_inheritance' : False,
        'collection'        : 'education',
    }

    _id = f.ObjectIdField( required=True, default=lambda: f.ObjectId() )

    school     = f.StringField()
    degree     = f.StringField()
    major      = f.StringField()
    start_time = f.DateTimeField()
    end_time   = f.DateTimeField()

    def to_dict(self):
        return {
            'school' : self.school,
            'degree' : self.degree,
            'major'  : self.major,
        }

