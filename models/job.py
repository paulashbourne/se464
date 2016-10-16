import mongoengine as me

class Job(me.Document):
    employer_id = me.ObjectIdField()

    position = me.StringField()
    description me.StringField()
    location = me.StringField()
    openings = me.IntField()

