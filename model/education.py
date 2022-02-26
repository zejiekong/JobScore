import json
from flask import request

from model.database import mongo

education_dao = mongo.db.education