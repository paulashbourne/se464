from tests.base import BaseTestCase
from tests.helper import *
from bson import ObjectId
import unittest
import ujson

from models import Employer, Job, User

class ApiTestCase(BaseTestCase, unittest.TestCase):

    @classmethod
    def check_resp(cls, resp, status = 200, data = None):
        assert resp.status_code == status

        if data is not None:
            resp_data = ujson.loads(resp.data)
            assert deep_equals(data, resp_data), "%s != %s" % (data, resp_data)

    def test_get_employer(self):
        print "test_get_employer"
        # First, create employer
        e = Employer(
            company_name = 'Foobar',
            website      = 'www.hello.com',
            emails       = [],
            email        = 'foo@bar.com',
            password     = User.encrypt_password('foobar'),
        )
        e.save()

        resp = self.app.get('/api/employer/%s' % e.id)
        self.check_resp(resp, 200, e.to_dict())

    def test_get_jobs(self):
        print "test_get_jobs"

        e = Employer(
            company_name = 'Barfoo',
            website      = 'www.goodbye.com',
            emails       = [],
            email        = 'bar@foo.com',
            password     = User.encrypt_password('barfoo'),
        )
        e.save()

        job1 = Job(
            employer_id   = e.id,
            position      = 'Software Engineer Intern',
            description   = 'Develop stuff.',
            location      = 'New York',
            openings      = 3
        )
        job2 = Job(
            employer_id   = e.id,
            position      = 'Developer Intern',
            description   = 'Develop more stuff',
            location      = 'San Francisco',
            openings      = 1
        )
        job1.save()
        job2.save()

        expected_results = [job1.to_dict(), job2.to_dict()]
        for row in expected_results:
            row['applications'] = []
        
        # Check employer ID
        resp = self.app.get('/api/jobs?employer_id=%s' % e.id)
        self.check_resp(resp, 200, expected_results)

        # Check location
        resp = self.app.get('/api/jobs?location=San%20Francisco')
        self.check_resp(resp, 200, [expected_results[1]])

if __name__ == '__main__':
    unittest.main()
