import mongoengine as me

class Employer(me.Document):
    company_name = me.StringField()
    website = me.StringField()

    # List of recruiter emails
    emails = me.ListField(me.StringField())
    # List of Job.id's
    job_postings = me.ListField(me.ObjectIdField())
