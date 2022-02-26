from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

import model.user
import model.education
<<<<<<< HEAD
import model.job
=======
>>>>>>> zejie

@app.route('/')
def index():
    return "Can connect"
