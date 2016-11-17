from flask import abort, g, render_template, request, session, url_for, redirect
from core.flaskwrap import Blueprint
from models import Experience
from models import Employer
from models import Job
from models import Student
from models import Application
from auth import student_login_required, employer_login_required
import bcrypt
from mongoengine import DoesNotExist

web = Blueprint('web', __name__)

@web.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html')

@web.errorhandler(403)
def page_forbidden(e):
    return render_template('pages/403.html')

@web.get('/')
def hello_world():
    return render_template('hello.html')

@web.get('/jobs/search')
def job_search():
    return render_template('job_search.html')

@web.get('/student/<student_id>/resume')
@student_login_required
def student_resume(student_id):
    if student_id != session['student_id']:
        # If the student id doesn't match the logged in user, redirect to their page
        return redirect(url_for('.student_resume', student_id=session['student_id']))

    student_info = g.user.to_dict()
    return render_template('student_resume.html', student_info=student_info)

@web.get('/employer/<employer_id>/new_job')
@employer_login_required
def new_job_posting(employer_id):
    return render_template('new_job_posting.html', employer_id=employer_id)

@web.get('/employer/<employer_id>/profile')
@employer_login_required
def employer_profile(employer_id):

    employer_info = map(lambda e: e.to_dict(), Employer.objects(id=employer_id))

    jobs = map(lambda job: job.to_dict(), Job.objects(employer_id=employer_id))

    return render_template('employer_profile.html', employer_info=employer_info, jobs=jobs)

@web.get('/employer/new_profile')
@employer_login_required
def new_employer_profile():
    return render_template('new_employer_profile.html')

def model_login(model, session_id, next_url):
    if session.get(session_id):
        return redirect(url_for(next_url), **{session_id: model_id})

    if request.method == 'GET':
        return render_template('login.html')

    session.clear()
    data = request.form
    email = data.get('email')
    password = data.get('password').encode('utf-8')

    try:
        model_instance = model.objects.get(email=email)
    except DoesNotExist:
        return render_template('login.html')

    if bcrypt.checkpw(password, model_instance.password.encode('utf-8')):
        model_id = str(model_instance.id)
        session[session_id] = model_id
        return redirect(url_for(next_url, **{session_id: model_id}))

    return render_template('login.html')

@web.route('/employers/login', methods=['GET', 'POST'])
def employer_login():
    return model_login(Employer, 'employer_id', '.employer_profile')

@web.route('/students/login', methods=['GET', 'POST'])
def student_login():
    return model_login(Student, 'student_id', '.student_resume')
