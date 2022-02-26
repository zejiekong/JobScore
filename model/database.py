from app import app
from flask_pymongo import PyMongo

app.config["MONGO_URI"] = "mongodb+srv://fsm:8K5D098sBbLveD8k@cluster0.ws3hh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo = PyMongo(app)