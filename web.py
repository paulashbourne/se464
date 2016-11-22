from flask import abort, g, render_template, request, session, url_for, redirect
from core.flaskwrap import Blueprint
from models import Experience
from models import Employer
from models import Job
from models import Student
from models import Application
from models.user import User
from auth import student_login_required, employer_login_required
import bcrypt
from mongoengine import DoesNotExist
from mongoengine.fields import ObjectId
from auth import student_login_required, employer_login_required, login_required

web = Blueprint('web', __name__)

@web.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html')

@web.errorhandler(403)
def page_forbidden(e):
    return render_template('pages/403.html')

@web.get('/')
def landing_page():
    if session.get('employer_id'):
        return redirect(url_for('.employer_profile',
                employer_id=session['employer_id']))
    if session.get('student_id'):
        return redirect(url_for('.student_resume',
                student_id=session['student_id']))
    return render_template('hello.html')

@web.get('/jobs/search')
@student_login_required
def job_search():
    return render_template('job_search.html', student_id=str(g.user.id))

@web.get('/student/<student_id>/resume/view')
@employer_login_required
def employer_view_student_resume(student_id):
    students = Student.objects(id=ObjectId(student_id))
    student = None
    for student in students:
        student_info = student.to_dict()
    if student is None:
        return "Not found", 404

    return render_template('student_resume.html',
            student_info=student_info, student_id=student_id, view=True)

@web.get('/student/<student_id>/resume')
@student_login_required
def student_resume(student_id):
    if student_id != session['student_id']:
        # If the student id doesn't match the logged in user, redirect to their page
        return redirect(url_for('.student_resume', student_id=session['student_id']))

    student_info = g.user.to_dict()
    return render_template('student_resume.html',
            student_info=student_info, student_id=student_id)

@web.get('/student/<student_id>/rankings')
@student_login_required
def student_rankings(student_id):
    applications = Application.objects(student_id=ObjectId(student_id))
    applications = map(lambda a: a.to_dict(), applications)

    for application in applications:
        job = Job.objects(id=ObjectId(application['job_id']))[0]
        application['job'] = job.to_dict()

    print applications

    return render_template('student_rankings.html',
        student_id=student_id,
        applications=applications
    )

@web.get('/employer/<employer_id>/rankings')
@employer_login_required
def employer_rankings(employer_id):
    rankings_array = []
    jobs = Job.objects(employer_id=ObjectId(employer_id))
    for job in jobs:
        applications = map(lambda a: a.to_dict(), Application.objects(job_id=job.id))
        job_dict = job.to_dict()
        job_dict['applications'] = applications
        rankings_array.append(job_dict)

    print rankings_array

    return render_template('employer_rankings.html',
        employer_id=employer_id,
        rankings_array=rankings_array
    )

@web.get('/employer/<employer_id>/new_job')
@employer_login_required
def new_job_posting(employer_id):
    return render_template('new_job_posting.html', employer_id=employer_id)

@web.get('/employer/<employer_id>/profile')
@employer_login_required
def employer_profile(employer_id):

    employer_info = map(lambda e: e.to_dict(), Employer.objects(id=employer_id))

    jobs = map(lambda job: job.to_dict(), Job.objects(employer_id=employer_id))

    print employer_info
    print jobs

    return render_template('employer_profile.html',
            employer_id=employer_id, employer_info=employer_info, jobs=jobs)

@web.get('/employer/new_profile')
@employer_login_required
def new_employer_profile():
    return render_template('new_employer_profile.html')

def model_login(model, model_name, next_url):
    session_id = model_name + '_id'
    if session.get(session_id):
        return redirect(url_for(next_url), **{session_id: model_id})

    if request.method == 'GET':
        return render_template('login.html', model_name=model_name)
    session.clear()
    data = request.form
    email = data.get('email')
    password = data.get('password').encode('utf-8')

    try:
        model_instance = model.objects.get(email=email)
    except DoesNotExist:
        return render_template('login.html', model_name=model_name)

    if bcrypt.checkpw(password, model_instance.password.encode('utf-8')):
        model_id = str(model_instance.id)
        session[session_id] = model_id
        return redirect(url_for(next_url, **{session_id: model_id}))

    return render_template('login.html', model_name=model_name)

@web.route('/employers/login', methods=['GET', 'POST'])
def employer_login():
    return model_login(Employer, 'employer', '.employer_profile')

@web.route('/students/login', methods=['GET', 'POST'])
def student_login():
    return model_login(Student, 'student', '.student_resume')
    

@web.route('/students/signup', methods=['GET', 'POST'])
def student_signup():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        email = data.get('email')
        password = data.get('password').encode('utf-8')
        new_student = {
            'name'     : name,
            'skills'   : [],
            'email'    : email,
            'password' : User.encrypt_password(password)
        }
        student = Student(**new_student)
        student.save()
        model_instance = Student.objects.get(email=email)
        model_id = str(model_instance.id)
        session_id = 'student_id'
        return redirect(url_for('.student_resume', **{session_id: model_id}))

    return render_template('signup.html')

@web.route('/students/logout', methods=['POST'])
def student_logout():
    session.clear()
    return redirect(url_for('.student_login'))

@web.route('/employers/logout', methods=['POST'])
def employer_logout():
    session.clear()
    return redirect(url_for('.employer_login'))
