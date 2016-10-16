from flask import Flask
from flask import render_template
from pymongo import MongoClient
client = MongoClient()

app = Flask(__name__)

db = client.se464

print db

@app.route('/')
def hello_world():
      return render_template('hello.html')
