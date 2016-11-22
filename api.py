from core.flaskwrap import Blueprint
from flask import request
from models.application import Application
from models.employer import Employer
from models.student import Student
from models.experience import Experience
from models.education import Education
from models.job import Job
import ujson
from bson import ObjectId
import mongoengine as me
import operator

api = Blueprint('api', __name__)

def save_model(model):
    try:
        model.save()
        return ujson.dumps(model.to_dict())
    except me.ValidationError:
        return "Validation error", 400
    except me.NotUniqueError:
        return "Not unique", 409

def models_to_dict(models):
    return map(lambda m: m.to_dict(), models)

@api.post('/employers')
def create_employer():
    data = request.json
    employer = Employer(**data)
    return save_model(employer)

@api.get('/employers/<employer_id>')
def get_employer(employer_id):
    employer_id = ObjectId(employer_id)
    employers = Employer.objects(id=employer_id)
    for employer in employers:
        return ujson.dumps(employer.to_dict())

    return "Not found", 404

@api.get('/employers')
def get_employers():
    employers = Employer.objects()
    return ujson.dumps(models_to_dict(employers))

@api.post('/students')
def create_student():
    data = request.json
    student = Student(**data)
    return save_model(student)

@api.get('/students/<student_id>')
def get_student(student_id):
    students = Student.objects(id=student_id)
    for student in students:
        return ujson.dumps(student.to_dict())

    return "Not found", 404

@api.post('/students/<student_id>/experience')
def add_experience(student_id):
    exp_data = request.form.to_dict()

    experience = Experience(**exp_data)
    students = Student.objects(id=student_id)
    for student in students:
        student.experience.append(experience)
        print student.experience
        return save_model(student)

    return "Not found", 404

@api.post('/students/<student_id>/education')
def add_education(student_id):
    student = Student.by_id(student_id)

    edu = request.form.to_dict()
    education = Education(**edu)
    students = Student.objects(id=student_id)
    for student in students:
        student.education.append(education)
        print student.education
        return save_model(student)

    return "Not found", 404

@api.post('/jobs')
def create_job():
    data = request.json
    job = Job(**data)
    return save_model(job)

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

@api.post('/jobs/<job_id>/apply/<student_id>')
def apply(job_id, student_id):
    data = request.json
    application = Application(
        job_id     = job_id,
        student_id = student_id,
    )
    return save_model(application)

def submit_rankings(data, ranking_type):
    if 'rankings' not in data:
        return "Bad Request", 400

    rankings = data['rankings']
    rankings_vals = rankings.values().sort()
    increasing = all(x<y for x, y in zip(rankings_vals, rankings_vals[1:]))
    if not increasing or rankings_vals[0] != 1:
        return "Invalid rankings", 409

    for app_id, rank in rankings:
        app = Application.by_id(app_id)                           
        if app is None:
            return "Invalid application ID", 400

        app.set(**{ranking_type : rank})

    return "OK", 200

@api.post('/students/<student_id>/rankings')
def submit_student_rankings(student_id):
    user = Student.by_id(student_id)
    if user is None:
        return "Invalid student ID", 400

    return submit_rankings(request.json, 'student_ranking')

@api.post('/employers/<employer_id>/rankings')
def submit_employer_rankings(id):
    user = Employer.by_id(id)
    if user is None:
        return "Invalid employer ID", 400

    return submit_rankings(request.json, 'employer_ranking')

