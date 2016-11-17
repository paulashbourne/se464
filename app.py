import flask
import auth

class Environment(object):
    DEVELOPMENT = 'dev'
    TESTING     = 'test'

class App(flask.Flask):

    def __init__(self, environment):
        super(App, self).__init__(__name__)

        self.environment = environment
        self.load_config()

        self.register_endpoints()

        self.db = None
        self.connect_db()
        self.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
        self.before_request(auth.before_request_handler)

    def load_config(self):
        from config import get_config
        config = get_config(self.environment)
        self.config.from_object(config)

    def register_endpoints(self):
        # Import and register handlers
        from web import web
        from api import api
        self.register_blueprint(web)
        self.register_blueprint(api, url_prefix='/api')

    def connect_db(self):
        import mongoengine
        self.db = mongoengine.connect(
            self.config['DB_NAME'],
            host     = self.config['DB_HOST'],
            port     = self.config['DB_PASSWORD'],
            username = self.config['DB_USER'],
            password = self.config['DB_PASSWORD'],
        )

    def drop_db(self):
        # Clear the current database - USE WITH CAUTION
        self.db.drop_database(self.config['DB_NAME'])

def main():
    # Listen for incoming connections
    app = App('dev')
    app.run()

if __name__ == "__main__":
    main()
