from app import App
from flask import render_template
from models.employer import Employer
from pymongo import MongoClient
import ujson
client = MongoClient()

app = App(__name__)

db = client.se464

print db

@app.get('/')
def hello_world():
    return render_template('hello.html')

@app.get('/student/<student_id>/resume')
def student_resume(student_id):
    student_info = {
        'name': 'Jeff Gulbronson',
        'experience': [
            {
                'title': 'Applications Developer Intern',
                'company': 'Pagerduty',
                'location': 'Toronto'
            }
        ]
    }

    return render_template('student_resume.html', student_info=student_info)

@app.get('/employer/<employer_id>')
def get_employer(employer_id):
    employer = Employer.find_by({ 'id' : employer_id })
    if employer is None:
        # TODO: throw error here
    
    return ujson.dumps(employer)

if __name__ == "__main__":
    app.run()
