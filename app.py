import flask
import auth
import os

class Environment(object):
    DEVELOPMENT = 'dev'
    TESTING     = 'test'
    PRODUCTION  = 'prod'

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
        if self.environment == 'prod':
            self.db = mongoengine.connect(
                self.config['DB_NAME'], host=self.config['DB_HOST']
            )
        else:
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
    if 'MONGODB_URI' in os.environ:
        app = App('prod')
    else:
        app = App('dev')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    main()
