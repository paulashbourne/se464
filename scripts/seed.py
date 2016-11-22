from datetime import datetime
from base import Script
from models.application import Application
from models.education import Education
from models.employer import Employer
from models.experience import Experience
from models.job import Job
from models.student import Student
from models.user import User
from random import choice

class SeedScript(Script):

    description = "Seed Script"

    def run(self):
        Employer.objects.delete()
        employers = self.get_employers()
        for e in employers:
            print "Creating employer %s" % e
            employer = Employer(**e)
            employer.save()

        Student.objects.delete()
        students = self.get_students()

        experiences = self.get_experiences()
        for i in range(len(experiences)):
            experience_list = experiences[i]
            s = students[i]
            for e in experience_list:
                s.experience = [Experience(**e)]
                s.save()

        educations = self.get_educations()
        for s in students:
            education = choice(educations)
            s.education = [Education(**education)]
            s.save()

        employers = Employer.find({})
        jobs = self.get_jobs()
        for i in range(len(jobs)):
            j = jobs[i]
            e = employers[i]
            j['employer_id'] = e['id']
            job = Job(**j)
            job.save()

        jobs = Job.find({})

        self.save_applications(jobs, students)

    def get_employers(self):
        return [
            {
                'company_name'  : 'Uber',
                'website'       : 'uber.com',
                'emails'        : [
                    'recruiter_1@uber.com',
                    'recruiter_2@uber.com',
                    'recruiter_3@uber.com'
                ],
                'email'         : 'waterloo@uber.com',
                'password'      : User.encrypt_password('uber')
            },
            {
                'company_name'  : 'Facebook',
                'website'       : 'facebook.com',
                'emails'        : [
                    'recruiter_1@facebook.com',
                    'recruiter_2@facebook.com',
                    'recruiter_3@facebook.com'
                ],
                'email'         : 'waterloo@facebook.com',
                'password'      : User.encrypt_password('facebook')
            },
            {
                'company_name'  : 'Google',
                'website'       : 'google.com',
                'emails'        : [
                    'recruiter_1@google.com'
                ],
                'email'         : 'waterloo@google.com',
                'password'      : User.encrypt_password('google')
            },
            {
                'company_name'  : 'Wish',
                'website'       : 'wish.com',
                'emails'        : [],
                'email'         : 'waterloo@wish.com',
                'password'      : User.encrypt_password('wish')
            },
            {
                'company_name'  : 'Snapchat',
                'website'       : 'snapchat.com',
                'emails'        : [
                    'recruiter_1@snapchat.com'
                ],
                'email'         : 'waterloo@snapchat.com',
                'password'      : User.encrypt_password('snapchat')
            }
        ]

    def get_educations(self):
        educations = [
            {
                'school'     :   'University of Waterloo',
                'degree'     :   'Bachelors',
                'major'      :   'Software Engineering',
                'start_time' :   datetime.strptime("1 Sep 13", "%d %b %y"),
                'end_time'   :   datetime.strptime("1 Jun 18", "%d %b %y")
            },
            {
                'school'     :   'University of Waterloo',
                'degree'     :   'Bachelors',
                'major'      :   'Mechatronics Engineering',
                'start_time' :   datetime.strptime("1 Sep 12", "%d %b %y"),
                'end_time'   :   datetime.strptime("1 Jun 17", "%d %b %y")
            },
            {
                'school'     :   'University of Waterloo',
                'degree'     :   'Bachelors',
                'major'      :   'Computer Science',
                'start_time' :   datetime.strptime("1 Sep 14", "%d %b %y"),
                'end_time'   :   datetime.strptime("1 Aug 19", "%d %b %y")
            }
        ]

        return educations

    def get_experiences(self):
        return [
            [
                {
                    'title'       :  'Web Developer Intern',
                    'company'     :  'Square',
                    'location'    :  'San Francisco',
                    'start_time'  :  datetime.strptime("30 Apr 16", "%d %b %y"),
                    'end_time'    :  datetime.strptime("01 Sep 16", "%d %b %y"),
                    'description' :  'Developed login and sign up flows'
                },
                {
                    'title'       :  'Software Engineer Intern',
                    'company'     :  'Spotify',
                    'location'    :  'New York',
                    'start_time'  :  datetime.strptime("1 Sep 15", "%d %b %y"),
                    'end_time'    :  datetime.strptime("17 Dec 15", "%d %b %y"),
                    'description' :  'Made lots of cool flows for music lovers'
                }
            ],
            [
                {
                    'title'       :  'Mobile Developer Intern',
                    'company'     :  'Pebble',
                    'location'    :  'Palo Alto',
                    'start_time'  :  datetime.strptime("30 Apr 16", "%d %b %y"),
                    'end_time'    :  datetime.strptime("01 Sep 16", "%d %b %y"),
                    'description' :  'Made Android app for Pebble Time'
                },
                {
                    'title'       : 'Software Engineer Intern',
                    'company'     : 'Google',
                    'location'    : 'New York',
                    'start_time'  :  datetime.strptime("1 Sep 15", "%d %b %y"),
                    'end_time'    :  datetime.strptime("17 Dec 15", "%d %b %y"),
                    'description' :  'Implemented search for the internet'
                }
            ],
            [
                {
                    'title'       :  'Backend Developer Intern',
                    'company'     :  'Xyz',
                    'location'    :  'Toronto',
                    'start_time'  :  datetime.strptime("30 Apr 16", "%d %b %y"),
                    'end_time'    :  datetime.strptime("01 Sep 16", "%d %b %y"),
                    'description' :  'Stored the alphabet in a database'
                },
                {
                    'title'       :  'Software Engineer Intern',
                    'company'     :  'Facebook',
                    'location'    :  'New York',
                    'start_time'  :  datetime.strptime("1 Sep 15", "%d %b %y"),
                    'end_time'    :  datetime.strptime("17 Dec 15", "%d %b %y"),
                    'description' :  'Connected 10billion people and made a few friends'
                },
                {
                    'title'       :  'Software Engineer Intern',
                    'company'     :  'Apple',
                    'location'    :  'Cupertino',
                    'start_time'  :  datetime.strptime("1 Jan 15", "%d %b %y"),
                    'end_time'    :  datetime.strptime("28 Apr 15", "%d %b %y"),
                    'description' :  'Hung out with Jony Ive'
                }
            ],
        ]

    def get_students(self):
        student_info = [
            ('Luke Skywalker', ['Python', 'Django', 'Postgres'], 'luke@uwaterloo.ca'),
            ('Darth Vader', ['Android', 'iOS', 'Java', 'Objective-C'], 'darth@uwaterloo.ca'),
            ('Thomas The Tankengine', ['Ruby', 'Rails'], 'thomas@uwaterloo.ca')
        ]

        for i in range(len(student_info)):
            info = student_info[i]
            print "Getting students. Name: %s" % info[0]
            student_dict = {
                'name'     : info[0],
                'skills'   : info[1],
                'email'    : info[2],
                'password' : User.encrypt_password('password')

            }
            student = Student(**student_dict)
            student.save()

        return Student.find({})

    def get_jobs(self):
        return [
            {
                'position'    : 'Software Engineer Intern',
                'description' : 'Work with a great team to build cool stuff',
                'location'    : 'Seattle',
                'openings'    : 5
            },
            {
                'position'    : 'Mobile Engineer Intern',
                'description' : 'Make Android and iOS applications',
                'location'    : 'New York',
                'openings'    : 2
            },
            {
                'position'    : 'Product Engineer Intern',
                'description' : 'Build a product for millions',
                'location'    : 'Palo Alto',
                'openings'    : 3
            },
            {
                'position'    : 'Software Engineer Intern',
                'description' : 'Develop web and backend systems for large amounts of data',
                'location'    : 'San Francisco',
                'openings'    : 3
            },
            {
                'position'    : 'Quality Assurance Engineer Intern',
                'description' : 'Optimize and extend quality assurance processes',
                'location'    : 'Hong Kong',
                'openings'    : 1
            }
        ]

    def save_applications(self, jobs, students):
        job_list = []
        for job in jobs:
            job_list.append(job)

        apps = [
            Application(job_id = job_list[0]['id'], student_id = students[0]['id']),
            Application(job_id = job_list[3]['id'], student_id = students[0]['id']),
            Application(job_id = job_list[4]['id'], student_id = students[0]['id']),
            Application(job_id = job_list[2]['id'], student_id = students[1]['id']),
            Application(job_id = job_list[1]['id'], student_id = students[1]['id']),
            Application(job_id = job_list[4]['id'], student_id = students[1]['id']),
            Application(job_id = job_list[0]['id'], student_id = students[2]['id']),
            Application(job_id = job_list[1]['id'], student_id = students[2]['id']),
            Application(job_id = job_list[2]['id'], student_id = students[2]['id']),
            Application(job_id = job_list[3]['id'], student_id = students[2]['id']),
            Application(job_id = job_list[4]['id'], student_id = students[2]['id'])
        ]

        for app in apps:
            app.save()

if __name__ == "__main__":
    SeedScript().main()
