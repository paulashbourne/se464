from tests.base import BaseTestCase
from bson import ObjectId
import unittest

class ApiTestCase(BaseTestCase):

    def test_get_employer(self):
        # First, create employer
        from models.employer import Employer
        e = Employer(
            company_name = 'Foobar'
        )
        e.save()

        resp = self.app.get('/api/employer/%s' % e.id)
        assert resp.status_code == 200
        import ipdb
        ipdb.set_trace()

if __name__ == '__main__':
    unittest.main()
