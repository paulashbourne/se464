from flask import render_template
from core.flaskwrap import Blueprint
from models import Experience

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
    student_info = {
        'student_id': student_id,
        'experience': map(lambda e: e.to_dict(), Experience.objects(student_id=student_id)),
        'education': []
    }

    return render_template('student_resume.html', student_info=student_info)


@web.get('/employer/<employer_id>/new_job')
def new_job_posting(employer_id):
    return render_template('new_job_posting.html', employer_id=employer_id)

@web.get('/employer/<employer_id>/profile')
def employer_profile(employer_id):
    return render_template('employer_profile.html')

@web.get('/employer/new_profile')
def new_employer_profile():
    return render_template('new_employer_profile.html')

