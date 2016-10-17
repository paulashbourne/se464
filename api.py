from core.flaskwrap import Blueprint
from flask import request
from models.application import Application
from models.employer import Employer
from models.job import Job
import ujson

api = Blueprint('api', __name__)

@api.post('/employer')
def create_employer():
    if 'employer' not in request.args:
        # TODO: throw error here
        pass

    employer = Employer.create(request.args.get('employer'))
    employer.save()

@api.get('/employer/<employer_id>')
def get_employer(employer_id):
    employer = Employer.find_by({ 'id' : employer_id })
    if employer is None:
        # TODO: throw error here
        pass

    return ujson.dumps(employer)

@api.post('/job')
def create_job():
    if 'job' not in request.args:
        # TODO: throw error
        pass

    job = Job.create(request.args.get('job'))
    job.save()

@api.get('/jobs')
def get_jobs():
    query = {}

    if 'employer_id' in request.args:
        query['employer_id'] = request.args.get('employer_id')

    if 'company_name' in request.args:
        query['company_name'] = request.args.get('company_name')

    if 'location' in request.args:
        query['location'] = request.args.get('location')

    jobs = Job.find(query)
    if jobs is None:
        # TODO: throw error
        pass
    job_ids = map(lambda job: job.id, jobs)

    # Get student applications for those jobs
    apps = Application.find({'job_id' : {'$in' : job_ids}})
    apps_by_job_id = dict(zip(map(lambda app: app.id, apps), apps))

    # Assemble results as dicts
    result = []
    for job in jobs:
        _dict = job.to_dict()
        _dict['application'] = application.to_dict()
        result.append(_dict)

    return ujson.dumps(result)

@api.post('/apply/<student_id>/<job_id>')
def apply(student_id, job_id):
    application = Application(
        student_id = student_id,
        job_id     = job_id
    )
    application.save()
