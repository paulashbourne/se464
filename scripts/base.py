import os
from app import App, Environment

class Script(object):

    description = "Some Script"

    def __init__(self, **kwargs):
        if 'MONGODB_URI' in os.environ:
            self.app = App(Environment.PRODUCTION)
        else:
            self.app = App(Environment.DEVELOPMENT)

    def run(self):
        # Should be defined in the script
        pass

    def main(self):
        self.run()

if __name__ == "__main__":
    Script().main()
