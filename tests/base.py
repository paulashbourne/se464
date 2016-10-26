import os
from app import App, Environment
import unittest
import tempfile

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        app = App(Environment.TESTING)
        app.db.drop_database(app.config['DB_NAME'])
        self.app = app.test_client()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
