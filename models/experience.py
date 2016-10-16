import mongoengine as me

class Experience(me.Document):
    title = me.StringField()
    company = me.StringField()
    location = me.StringField()

    start_time = me.DateTimeField()
    end_time = me.DateTimeField()

    description = me.ListField(me.StringField())
