# Contains handlers for API Endpoints

from core.flaskwrap import Blueprint
from flask import request, redirect, url_for, g
from models.application import Application
from models.employer import Employer
from models.student import Student
from models.experience import Experience
from models.education import Education
from models.job import Job
import ujson
from bson import ObjectId
import mongoengine as me
from auth import student_login_required, employer_login_required, login_required
import operator

api = Blueprint('api', __name__)

# Attempts to save a model, catching errors if they occur and throwing an
# appropriate HTTP error
def save_model(model):
    try:
        model.save()
        return ujson.dumps(model.to_dict())
    except me.ValidationError:
        return "Validation error", 400
    except me.NotUniqueError:
        return "Not unique", 409

# Helper function: convert a list of models to a list of dicts
def models_to_dict(models):
    return map(lambda m: m.to_dict(), models)

@api.post('/employers')
def create_employer():
    data = request.json
    employer = Employer(**data)
    return save_model(employer)

@api.get('/employers/<employer_id>')
@login_required
def get_employer(employer_id):
    employer_id = ObjectId(employer_id)
    employers = Employer.objects(id=employer_id)
    for employer in employers:
        return ujson.dumps(employer.to_dict())

    return "Not found", 404

@api.get('/employers')
@login_required
def get_employers():
    employers = Employer.objects()
    return ujson.dumps(models_to_dict(employers))

@api.post('/students')
def create_student():
    data = request.json
    student = Student(**data)
    return save_model(student)

@api.get('/students/<student_id>')
@login_required
def get_student(student_id):
    students = Student.objects(id=student_id)
    for student in students:
        return ujson.dumps(student.to_dict())

    return "Not found", 404

@api.post('/students/<student_id>/experience')
@student_login_required
def add_experience(student_id):
    exp_data = request.form.to_dict()

    experience = Experience(**exp_data)
    students = Student.objects(id = student_id)
    for student in students:
        student.experience.append(experience)
        return save_model(student)

    return "Not found", 404

@api.post('/students/<student_id>/education')
@student_login_required
def add_education(student_id):
    student = Student.by_id(student_id)

    edu = request.form.to_dict()
    education = Education(**edu)
    students = Student.objects(id = student_id)
    for student in students:
        student.education.append(education)
        return save_model(student)

    return "Not found", 404

@api.post('/jobs')
@employer_login_required
def create_job():
    data = request.form.to_dict()
    job = Job(**data)
    return save_model(job)

@api.get('/jobs')
@login_required
def get_jobs():
    query = {}
    request_data = request.args.to_dict()

    # Search by id
    if 'employer_id' in request_data:
        query['employer_id'] = ObjectId(request.args.get('employer_id'))

    # Search by location
    if 'company_name' in request_data:
        company_name = request_data.get('company_name')
        employer = Employer.find_one({'company_name' : company_name})
        if employer:
            query['employer_id'] = employer.id
        else:
            query['company_name'] = '-1'

    # Search by location
    if 'location' in request_data:
        query['location'] = request_data.get('location')

    # Execute query
    jobs = Job.find(query)

    job_ids = map(lambda job: job.id, jobs)

    # Get student applications for those jobs
    app_query = {
        'job_id' : {'$in' : job_ids}
    }

    # If I'm a student, only return my apps
    if g.student:
        app_query['student_id'] = g.user.id

    # Query for applications to those jobs
    apps = Application.find(app_query)

    # Convert to dictionary based on either student or employer context
    if g.student:
        apps = map(lambda app: app.to_dict_student(), apps)
    else:
        apps = map(lambda app: app.to_dict_employer(), apps)

    apps_by_job_id = dict(zip(map(lambda app: app['job_id'], apps), apps))

    # Assemble results as dicts
    result = []
    for job in jobs:
        _dict = job.to_dict()
        _dict['application'] = apps_by_job_id.get(str(job.id))
        result.append(_dict)

    return ujson.dumps(result)

@api.post('/jobs/<job_id>/apply/<student_id>')
@student_login_required
def apply(job_id, student_id):
    data = request.json
    application = Application(
        job_id     = job_id,
        student_id = student_id,
    )
    return save_model(application)

# Helper function
def submit_rankings(data, ranking_type):
    if 'rankings' not in data:
        return "Bad Request", 400

    rankings = data['rankings']
    rankings_vals = sorted(map(lambda v: int(v), rankings.values()))

    # Validate rankings - monotonically increasing integers from 1 to n
    if len(rankings) > 1:
        increasing = all(x<y for x, y in zip(rankings_vals, rankings_vals[1:]))
        if not increasing or rankings_vals[0] != 1:
            return "Invalid rankings", 409

    for app_id in rankings:
        rank = rankings.get(app_id)
        app = Application.by_id(ObjectId(app_id))
        if app is None:
            return "Invalid application ID", 400

        app.set(**{ranking_type : rank})

    return 200

@api.post('/students/<student_id>/rankings')
def submit_student_rankings(student_id):
    user = Student.by_id(student_id)
    if user is None:
        return "Invalid student ID", 400

    data = {
        'rankings': request.form.to_dict()
    }

    rankings_result = submit_rankings(data, 'student_ranking')

    if rankings_result == 200:
        return redirect(url_for('web.student_rankings',
            student_id=student_id))
    else:
        return rankings_result

@api.post('/employers/<employer_id>/rankings')
def submit_employer_rankings(employer_id):
    user = Employer.by_id(ObjectId(employer_id))
    if user is None:
        return "Invalid employer ID", 400

    data = {
        'rankings': request.form.to_dict()
    }

    rankings_result = submit_rankings(data, 'employer_ranking')

    if rankings_result == 200:
        return redirect(url_for('web.employer_rankings',
            employer_id=employer_id))
    else:
        return rankings_result
