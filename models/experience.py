from mongoengine import fields as f
from bson.objectid import ObjectId

class Experience(f.EmbeddedDocument):
    _id = f.ObjectIdField( required=True, default=lambda: ObjectId() )
    title      = f.StringField(required = True)
    company    = f.StringField(required = True)
    location   = f.StringField()

    start_time = f.DateTimeField()
    end_time   = f.DateTimeField()

    description = f.StringField(default='')

    def to_dict(self):
        return {
            'id': str(self._id),
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'description': self.description
        }

