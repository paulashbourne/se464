from tests.base import BaseTestCase
from bson import ObjectId
import unittest
import ujson

class ApiTestCase(BaseTestCase):

    @classmethod
    def list_deep_equals(cls, expected, test):
        if len(l1) != len(l2):
            return False
        from itertools import zip
        for v1, v2 in zip(sorted(expected), sorted(test)):
            if type(v1) != type(v2):
                return False
            if isinstance(v1, list):
                return cls.list_deep_equals(v1, v2)
            elif isinstance(v1, dict):
                return cls.dict_deep_equals(v1, v2)
            elif v1 != v2:
                return False
        return True

    @classmethod
    def dict_deep_equals(cls, expected, test):
        if len(expected.keys()) != len(test.keys()):
            return False
        for key, value in expected.iteritems():
            if key not in test:
                return False
            if value != test[key]:
                # Might be objects/dicts/lists - recurse
                if isinstance(value, dict):
                    if not cls.dict_deep_equals(value, test[key]):
                        return False
                elif isinstance(value, list):
                    if not cls.list_deep_equals(value, test[key]):
                        return False
                else:
                    return False
        return True


    @classmethod
    def check_resp(cls, resp, status = 200, data = None):
        assert resp.status_code == status

        if data is not None:
            resp_data = ujson.loads(resp.data)
            assert cls.dict_deep_equals(data, resp_data)

    def test_get_employer(self):
        # First, create employer
        from models.employer import Employer
        fields = {
            'company_name' : 'Foobar',
            'website'      : 'www.hello.com',
            'emails'       : []
        }
        e = Employer(**fields)
        e.save()

        resp = self.app.get('/api/employer/%s' % e.id)
        self.check_resp(resp, 200, e.to_dict())

if __name__ == '__main__':
    unittest.main()
