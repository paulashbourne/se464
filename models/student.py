import mongoengine as me

class Student(me.Document):
    name = me.StringField()

    # List of Education.id's
    education = me.ListField(me.ObjectIdField())
    # List of Experience.id's
    experience = me.ListField(me.ObjectIdField())

    # i.e. Python, Flask, React, etc.
    skills = me.ListField(me.StringField())
