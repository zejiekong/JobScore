from app import app
import json
from flask import request

from model.database import mongo

class User:
    def __init__(self):
        self.user_dao = mongo.db.users
    

    def create(self, user_dict):
        self.user_dao.insert_one(user_dict)


    def update(self, user_dict, updated_user):
        condition = {"username": user_dict.get("username")}
        self.user_dao.update_one(condition, {"$set": updated_user})


    def get(self, user_dict):
        condition = {"username": user_dict.get('username')}
        user = self.user_dao.find_one(condition)
        return user


    def get_all(self):
        users = self.user_dao.find()
        return users


    def delete(self, user_dict):
        self.user_dao.delete_one(user_dict)


    def delete_many(self, user_dict):
        self.user_dao.delete_many(user_dict)

@app.route('/demo')
def demo():
    user = User()
    print("create user oong")
    user_dict = {
        "username": "oong",
        "full_name": "Oong Jie Xiang",
        "email": "oongjiexiang@yahoo.com",
        "password": "this will fail"
    }
    user.create(user_dict)

    print("get user oong")
    print(user.get({"username": "oong"}))

    print("update user oong to jie")
    updated_user_dict = {
        "username": "jie",
        "full_name": "Oong",
        "email": "oongjiexiang@gmail.com",
        "password": "this will not fail"
    }
    user.update({"username": "oong"}, updated_user_dict)

    print("create user jack")
    user_dict = {
        "username": "jack",
        "full_name": "Jack Chong",
        "email": "jack@gmail.com",
        "password": "this will not fail"
    }
    user.create(user_dict)

    print("get all users")
    print(user.get_all())

    print("delete user jack")
    user.delete({"username": "jack"})

    print("get all users again")
    print(user.get_all())

    return "ok"
