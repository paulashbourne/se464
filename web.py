from flask import render_template
from core.flaskwrap import Blueprint
from models import Experience
from models import Employer
from models import Job
from models import Student
from models import Application
from auth import student_login_required, employer_login_required

web = Blueprint('web', __name__)

@web.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html')

@web.get('/')
def hello_world():
    return render_template('hello.html')

@web.get('/jobs/search')
def job_search():
    return render_template('job_search.html')

@web.get('/student/<student_id>/resume')
def student_resume(student_id):
    students = Student.objects(id=student_id)
    for student in students:
        student_info = student.to_dict()
        return render_template('student_resume.html', student_info=student_info)

    return render_template('pages/404.html')


@web.get('/employer/<employer_id>/new_job')
@employer_login_required
def new_job_posting(employer_id):
    return render_template('new_job_posting.html', employer_id=employer_id)

@web.get('/employer/<employer_id>/profile')
def employer_profile(employer_id):

    employer_info = map(lambda e: e.to_dict(), Employer.objects(id=employer_id))

    jobs = map(lambda job: job.to_dict(), Job.objects(employer_id=employer_id))

    return render_template('employer_profile.html', employer_info=employer_info, jobs=jobs)

@web.get('/employer/new_profile')
def new_employer_profile():
    return render_template('new_employer_profile.html')

@web.get('/employers/login')
def employer_login():
    return 'Employer login page'

@web.get('/students/login')
def student_login():
    return 'Employer login page'
