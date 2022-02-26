from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://fsm:8K5D098sBbLveD8k@cluster0.ws3hh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
def index():
    return "Can connect"