from mongoengine import fields as f

class Education(f.EmbeddedDocument):
    meta = {
        'allow_inheritance' : False,
        'collection'        : 'education',
    }

    _id = f.ObjectIdField( required=True, default=lambda: ObjectId() )

    school     = f.StringField()
    degree     = f.StringField()
    major      = f.StringField()
    start_time = f.DateTimeField()
    end_time   = f.DateTimeField()

    def to_dict(self):
        return {
            'id': str(self._id),
            'school': self.school,
            'degree': self.degree,
            'major': self.major
        }

