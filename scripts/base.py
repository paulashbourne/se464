from core.db import connect_db

class Script(object):

    description = "Some Script"

    def __init__(self, **kwargs):
        connect_db()

    def run(self):
        # Should be defined in the script
        pass
