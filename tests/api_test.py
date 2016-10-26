from tests.base import BaseTestCase
from bson import ObjectId
import unittest

class ApiTestCase(BaseTestCase):

    def test_get_employer(self):
        resp = self.app.get('/api/employer/%s' % ObjectId())
        assert resp.status_code == 200

if __name__ == '__main__':
    unittest.main()
