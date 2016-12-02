import flask
import auth
import os

# A string enum defining different environments
class Environment(object):
    DEVELOPMENT = 'dev'
    TESTING     = 'test'
    PRODUCTION  = 'prod'

# App class inherits from a standard Flask app
class App(flask.Flask):

    def __init__(self, environment):
        super(App, self).__init__(__name__)

        # Load config
        self.environment = environment
        self.load_config()

        # Register endpoints
        self.register_endpoints()
        self.before_request(auth.before_request_handler)

        # Init DB
        self.db = None
        self.connect_db()

        # Secret key - used to cryptographically sign cookies
        self.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    # Load config based on self.environment
    def load_config(self):
        from config import get_config
        config = get_config(self.environment)
        self.config.from_object(config)

    # Attach endpoint blueprints
    def register_endpoints(self):
        # Import and register handlers
        from web import web
        from api import api
        self.register_blueprint(web)
        self.register_blueprint(api, url_prefix='/api')

    # Connects to the datbase
    def connect_db(self):
        import mongoengine
        self.db = mongoengine.connect(
            self.config['DB_NAME'],
            host     = self.config['DB_HOST'],
            port     = self.config['DB_PASSWORD'],
            username = self.config['DB_USER'],
            password = self.config['DB_PASSWORD'],
        )

    # DROP the current database - USE WITH CAUTION, IRREVERSIBLE
    def drop_db(self):
        self.db.drop_database(self.config['DB_NAME'])

def main():
    # If MONGODB_URI environment variable is defined,
    # Load production conifg
    # Otherwise, default to development config
    if 'MONGODB_URI' in os.environ:
        app = App(Environment.PRODUCTION)
    else:
        app = App(Environment.DEVELOPMENT)


    # Listen for incoming connections
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    main()
