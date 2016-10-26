from tests.base import BaseTestCase
from bson import ObjectId
import unittest
import ujson

class ApiTestCase(BaseTestCase):

    @classmethod
    def deep_equals(cls, val1, val2):
        if val1 == val2:
            # Try naive compare first
            return True
        if type(val1) == dict:
            if type(val2) != dict:
                return False
            return cls.dict_deep_equals(val1, val2)
        elif type(val1) == list:
            if type(val2) != list:
                return False
            return cls.list_deep_equals(val1, val2)
        return False

    @classmethod
    def list_deep_equals(cls, expected, test):
        if len(expected) != len(test):
            return False
        for v1, v2 in zip(sorted(expected), sorted(test)):
            return cls.deep_equals(v1, v2)
        return True

    @classmethod
    def dict_deep_equals(cls, expected, test):
        if len(expected.keys()) != len(test.keys()):
            return False
        for key, value in expected.iteritems():
            if key not in test:
                return False
            return cls.deep_equals(value, test[key])
        return True


    @classmethod
    def check_resp(cls, resp, status = 200, data = None):
        assert resp.status_code == status

        if data is not None:
            resp_data = ujson.loads(resp.data)
            assert cls.deep_equals(data, resp_data), "%s != %s" % (data, resp_data)

    def test_get_employer(self):
        # First, create employer
        from models.employer import Employer
        e = Employer(
            company_name = 'Foobar',
            website      = 'www.hello.com',
            emails       = []
        )
        e.save()

        resp = self.app.get('/api/employer/%s' % e.id)
        self.check_resp(resp, 200, e.to_dict())

    def test_get_jobs(self):
        from models.employer import Employer
        from models.job import Job

        e = Employer(
            company_name = 'Barfoo',
            website      = 'www.goodbye.com',
            emails       = []
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
