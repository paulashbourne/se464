from flask import render_template
from core import Blueprint

web = Blueprint('web', __name__)

@web.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html')

@web.get('/')
def hello_world():
    return render_template('hello.html')

@web.get('/student/<student_id>/resume')
def student_resume(student_id):
    student_info = {
        'name': 'Jeff Gulbronson',
        'education': [
            {
                'degree': 'Bachelor of Software Engineering fdsdfslkjf',
                'school': 'University of Waterloo'
            }
        ],
        'experience': [
            {
                'title': 'Applications Developer Intern',
                'company': 'Pagerduty',
                'location': 'Toronto',
                'description': [
                    'Part of the regular on-call schedule, triaging and repairing issues from alerts',
                    'Helped architect a MySQL to Kafka data pump, to provide transactional Kafka publishes',
                    'Gained experience building and maintaining distributed systems, using tools such as Kafka, Zookeeper and Mesos/Marathon',
                    'Knowledgable in developing concurrent programs using the actor-model of programming'
                ]
            },
            {
                'title': 'Applications Developer Intern',
                'company': 'Pagerduty',
                'location': 'Toronto',
                'description': [
                    'Part of the regular on-call schedule, triaging and repairing issues from alerts',
                    'Helped architect a MySQL to Kafka data pump, to provide transactional Kafka publishes',
                    'Gained experience building and maintaining distributed systems, using tools such as Kafka, Zookeeper and Mesos/Marathon',
                    'Knowledgable in developing concurrent programs using the actor-model of programming'
                ]
            }

        ]
    }

    return render_template('student_resume.html', student_info=student_info)


@web.get('/employer/new_job')
def new_job_posting():
    return render_template('new_job_posting.html')