import mongoengine as me

class Education(me.Document):
    school = me.StringField()
    degree = me.StringField()

    start_time = me.DateTimeField()
    end_time = me.DateTimeField()
