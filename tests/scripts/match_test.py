from tests.base import BaseTestCase
from tests.helper import *
from bson import ObjectId
import unittest

from models.job import Job
from models.application import Application
from models.student import Student
from scripts.match import MatchScript

class MatchTestCase(BaseTestCase):

    @classmethod
    def get_test_case(cls):
        jobs = [
            # Should be filled
            Job(
                id  = ObjectId(),
                employer_id = ObjectId(),
                position    = "Software Engineer",
                description = "We're hiring software engineers!",
                location    = "Mountain View, CA",
                openings    = 1,
            ),
            # Should be partially filled
            Job(
                id  = ObjectId(),
                employer_id = ObjectId(),
                position    = "Software Engineer",
                description = "We're hiring software engineers!",
                location    = "Mountain View, CA",
                openings    = 3,
            ),
            # Should be unmatched
            Job(
                id  = ObjectId(),
                employer_id = ObjectId(),
                position    = "Test Engineer",
                description = "We're hiring software engineers!",
                location    = "Mountain View, CA",
                openings    = 1,
            )
        ]

        students = [
            # This student should get job[0]
            Student(
                id       = ObjectId(),
                name     = "John GetsMyFirstPick",
                email    = "s0@test.com",
                password = "passwordhash",
            ),
            # This student should get job[1]
            Student(
                id       = ObjectId(),
                name     = "John GetsMySecondPick",
                email    = "s1@test.com",
                password = "passwordhash",
            ),
            # This student should get job[1]
            Student(
                id       = ObjectId(),
                name     = "John GetsAnotherJob",
                email    = "s2@test.com",
                password = "passwordhash",
            ),
            # This student does not get matched
            Student(
                id       = ObjectId(),
                name     = "John DoesntGetAJob",
                email    = "s3@test.com",
                password = "passwordhash",
            )
        ]

        apps = [
            # student[0]'s applications
            # app to job [0]
            Application(
                id               = ObjectId(),
                job_id           = jobs[0].id,
                student_id       = students[0].id,
                student_ranking  = 1,
                employer_ranking = 1,
            ),
            # app to job[1]
            Application(
                id               = ObjectId(),
                job_id           = jobs[1].id,
                student_id       = students[0].id,
                student_ranking  = 2,
                employer_ranking = 2,
            ),
            # app to job [2]
            Application(
                id               = ObjectId(),
                job_id           = jobs[2].id,
                student_id       = students[0].id,
                student_ranking  = 3,
                employer_ranking = 2,
            ),
            # student[1]'s applications
            # app to job [0]
            # app to job [2]
            Application(
                id               = ObjectId(),
                job_id           = jobs[2].id,
                student_id       = students[1].id,
                student_ranking  = 3,
                employer_ranking = 1,
            ),
            Application(
                id               = ObjectId(),
                job_id           = jobs[0].id,
                student_id       = students[1].id,
                student_ranking  = 1,
                employer_ranking = 2,
            ),
            # app to job[1]
            Application(
                id               = ObjectId(),
                job_id           = jobs[1].id,
                student_id       = students[1].id,
                student_ranking  = 2,
                employer_ranking = 3,
            ),
            # student[2]'s applications
            # app to job [0]
            Application(
                id               = ObjectId(),
                job_id           = jobs[0].id,
                student_id       = students[2].id,
                student_ranking  = 2,
                employer_ranking = 3,
            ),
            # app to job[1]
            Application(
                id               = ObjectId(),
                job_id           = jobs[1].id,
                student_id       = students[2].id,
                student_ranking  = 1,
                employer_ranking = 4,
            ),
            # app to job [2]
            Application(
                id               = ObjectId(),
                job_id           = jobs[2].id,
                student_id       = students[2].id,
                student_ranking  = 3,
                employer_ranking = None,
            ),
            # student[3]'s applications
            # app to job[1]
            Application(
                id               = ObjectId(),
                job_id           = jobs[1].id,
                student_id       = students[2].id,
                student_ranking  = None,
                employer_ranking = 1,
            ),
            # app to job [0]
            Application(
                id               = ObjectId(),
                job_id           = jobs[0].id,
                student_id       = students[2].id,
                student_ranking  = 2,
                employer_ranking = 4,
            ),
            # app to job [2]
            Application(
                id               = ObjectId(),
                job_id           = jobs[2].id,
                student_id       = students[2].id,
                student_ranking  = 1,
                employer_ranking = None,
            ),
        ]
        # Sort apps by employer ranking (as required by function spec)
        apps = sorted(apps, key = lambda a: a.employer_ranking)

        return jobs, students, apps

    def test_match_jobs(self):

        jobs, students, apps = self.get_test_case()

        offers, partially_matched, unmatched = MatchScript.match_jobs(jobs, apps)

        # Check offers
        assert offers[students[0].id].job_id == jobs[0].id, "student[0] should get job[0]"
        assert offers[students[1].id].job_id == jobs[1].id, "student[1] should get job[1]"
        assert offers[students[2].id].job_id == jobs[1].id, "student[2] should get job[1]"
        assert students[3].id not in offers, "student[2] should not get matched"

        # Check partial matches
        assert len(partially_matched) == 1, "Only job[1] should be partially matched!"
        assert partially_matched[0].id == jobs[1].id, "Only job[1] should be partially matched!"
        # Check unmatched
        assert len(unmatched) == 1, "Only job[2] should be partially unmatched!"
        assert unmatched[0].id == jobs[2].id, "Only job[2] should be unmatched!"

    def test_run(self):
        jobs, students, apps = self.get_test_case()

        # Add the test objects to DB
        for obj in jobs + students + apps:
            obj.save()

        # Run the script
        MatchScript(app = self.app).run()

        # Check job objects
        job_ids = map(lambda job: job.id, jobs)
        db_jobs = Job.by_ids_dict(job_ids)
        assert(db_jobs[jobs[0].id].state == Job.State.FILLED)
        assert(db_jobs[jobs[1].id].state == Job.State.PARTIALLY_FILLED)
        assert(db_jobs[jobs[2].id].state == Job.State.UNFILLED)

        # Check app objects
        expected_matches = {
            students[0].id : jobs[0].id,
            students[1].id : jobs[1].id,
            students[2].id : jobs[1].id,
            students[3].id : None
        }
        app_ids = map(lambda app: app.id, apps)
        db_apps = Application.by_ids(app_ids)
        for app in db_apps:
            if expected_matches[app.student_id] == app.job_id:
                assert(app.state == Application.State.MATCHED)
            else:
                assert(app.state == Application.State.NOT_MATCHED)

if __name__ == '__main__':
    unittest.main()
