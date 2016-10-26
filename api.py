from core.flaskwrap import Blueprint
from flask import request
from models.application import Application
from models.employer import Employer
from models.experience import Experience
from models.job import Job
import ujson
from bson import ObjectId

api = Blueprint('api', __name__)

@api.post('/employer')
def create_employer():
    data = ujson.loads(request.data)
    if 'employer' not in data:
        # TODO: throw error here
        pass

    employer = Employer(**data.get('employer'))
    employer.save()
    return ujson.dumps(employer.to_dict())

@api.get('/employer/<employer_id>')
def get_employer(employer_id):
    employer_id = ObjectId(employer_id)
    employer = Employer.by_id(employer_id)
    if employer is None:
        # TODO: throw error here
        pass

    return ujson.dumps(employer.to_dict())

@api.post('/student/<student_id>/experience')
def add_experience(student_id):
    exp_data = request.form.to_dict()
    exp_data['student_id'] = student_id
    print exp_data

    experience = Experience(**exp_data)
    experience.save()
    return ujson.dumps(experience.to_dict())

@api.post('/student/<student_id>/education')
def add_education(student_id):
    student = Student.by_id(student_id)

    edu = request.args.data
    education = Education(**edu)
    education.save()

    student['education'].append(education['id'])
    student.save()

@api.post('/jobs')
def create_job():
    print request.form.to_dict()
    data = request.form.to_dict()
    job = Job(**data)
    job.save()
    return ujson.dumps(job.to_dict())

@api.get('/jobs')
def get_jobs():
    query = {}

    request_data = request.args.to_dict()
    print request_data
    if 'employer_id' in request_data:
        query['employer_id'] = ObjectId(request.args.get('employer_id'))

    if 'company_name' in request_data:
        company_name = request_data.get('company_name')
        print company_name
        for company in Employer.find({'company_name': company_name}):
            print company
            query['employer_id'] = company.id
            break
        else:
            query['company_name'] = '-1'

    if 'location' in request_data:
        query['location'] = request_data.get('location')

    jobs = Job.find(query)
    if jobs is None:
        # TODO: throw error
        pass
    job_ids = map(lambda job: job.id, jobs)

    # Get student applications for those jobs
    apps = Application.find({'job_id' : {'$in' : job_ids}})
    apps = map(lambda app: app.to_dict(), apps)
    apps_by_job_id = dict(zip(map(lambda app: app['job_id'], apps), apps))

    # Assemble results as dicts
    result = []
    for job in jobs:
        _dict = job.to_dict()
        _dict['application'] = apps_by_job_id.get(str(job.id))
        result.append(_dict)

    return ujson.dumps(result)

@api.post('/apply/<student_id>/<job_id>')
def apply(student_id, job_id):
    application = Application(
        student_id = ObjectId(student_id),
        job_id     = ObjectId(job_id)
    )
    application.save()
    return ujson.dumps(application);
