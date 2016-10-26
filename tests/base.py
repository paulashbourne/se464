import os
from app import app
import unittest
import tempfile

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        from core.db import connect_db
        connect_db()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
