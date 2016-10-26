from core.flaskwrap import App
import ujson

app = App(__name__)

# Import and register handlers
from web import web
from api import api
app.register_blueprint(web)
app.register_blueprint(api, url_prefix='/api')

def main():

    # Connect to the database
    from core.db import connect_db
    connect_db()

    # Listen for incoming connections
    app.run()

if __name__ == "__main__":
    main()
