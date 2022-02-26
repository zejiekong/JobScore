from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

import model.user
import model.education
import model.job

@app.route('/')
def index():
    return "Can connect"
