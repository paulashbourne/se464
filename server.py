from app import App
from flask import render_template
from pymongo import MongoClient
client = MongoClient()

app = App(__name__)

db = client.se464

print db

@app.get('/')
def hello_world():
    return render_template('hello.html')

@app.route('/student/<student_id>/resume')
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

if __name__ == "__main__":
    app.run()
