from mongoengine import fields as f

class Experience(f.EmbeddedDocument):
    title      = f.StringField(required = True)
    company    = f.StringField(required = True)
    location   = f.StringField()

    start_time = f.DateTimeField()
    end_time   = f.DateTimeField()

    description = f.StringField()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'description': self.description
        }

