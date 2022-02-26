from flask import Flask,render_template,redirect,url_for,request,session
from flask_pymongo import PyMongo

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["MONGO_URI"] = "mongodb+srv://fsm:8K5D098sBbLveD8k@cluster0.ws3hh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

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

@app.route("/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        error = "User not found"
        #check user and password
        user_dict = {}
        for i in list(user.get_all()):
            if request.form["uname"] == i["username"]: #check in database
                user_dict = i
                break
        if user_dict != {}:
            if request.form["psw"] == user_dict["password"]: #check in database
                session['username'] = request.form["uname"]
                return redirect(url_for('home'))
            else:
                error = "Incorrect Password"
        return render_template("login.html",error=error)

    else:
        return render_template("login.html",error="None")

@app.route("/registration",methods=["GET","POST"])
def registration():
    if request.method == "POST":
        for i in list(user.get_all()):
            if request.form["uname"] == i["username"]: #check exisiting or not
                error = "username already exists"
                return render_template("register.html",error="None")
        
        #write into database
        user_dict = {
            "username": request.form["uname"],
            "full_name": request.form["fullname"],
            "password": request.form["psw"]
        }
        
        user.create(user_dict)
        
        #request.form["loca"]
        #request.form["salary"]
        #request.form["interest"]
        return redirect(url_for('login'))
        #register user credentials
    else:
        return render_template("register.html",error="None")

@app.route("/home",methods=["GET","POST"])
def home():
    # if request.method == "POST":

    # else:
    return render_template("home.html")

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))

if __name__ == "__main__":
    mongo = PyMongo(app)
    user = User()
    app.run()   