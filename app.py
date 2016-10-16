from core import App
from models.employer import Employer
from pymongo import MongoClient
import ujson
client = MongoClient()

app = App(__name__)

db = client.se464

def main():
    # Import and register handlers
    from web import web
    from api import api
    app.register_blueprint(web)
    app.register_blueprint(api, url_prefix='/api')

    # Listen for incoming connections
    app.run()

print db

if __name__ == "__main__":
    main()
