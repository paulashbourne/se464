from flask import g, session, redirect, url_for, request
from functools import wraps
from random import randint
from models import Employer, Student

def before_request_handler():
    if 'employer_id' in session:
        employers = Employer.objects(id=session['employer_id'])
        for employer in employers:
            g.user = employer
            g.employer = True
            g.student = False
    elif 'student_id' in session:
        students = Student.objects(id=session['student_id'])
        for student in students:
            g.user = student
            g.student = True
            g.employer = False
    else:
        g.employer = False
        g.student = False
        g.user = False

def student_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.student:
           return redirect(url_for('web.student_login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def employer_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.employer:
           return redirect(url_for('web.employer_login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
