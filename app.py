from core import App
from models.employer import Employer
from pymongo import MongoClient
import ujson
import mongoengine

app = App(__name__)

mongoengine.connect('se464', alias='default')

def main():
    # Import and register handlers
    from web import web
    from api import api
    app.register_blueprint(web)
    app.register_blueprint(api, url_prefix='/api')

    # Listen for incoming connections
    app.run()

if __name__ == "__main__":
    main()
