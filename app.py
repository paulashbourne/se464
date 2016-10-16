from core.flaskwrap import App
from models.employer import Employer
import ujson

app = App(__name__)

def main():
    # Import and register handlers
    from web import web
    from api import api
    app.register_blueprint(web)
    app.register_blueprint(api, url_prefix='/api')

    # Connect to the database
    from core.db import connect_db
    connect_db()

    # Listen for incoming connections
    app.run()

if __name__ == "__main__":
    main()
