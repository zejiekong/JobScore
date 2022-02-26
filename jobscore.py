from flask import Flask,render_template,redirect,url_for,request,session
from model.user import User

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        error = "User not found"
        #check user and password
        for i in user.get_all:
            if request.form["uname"] == i["username"]: #check in database
                return render_template("login.html",error=error)
        if request.form["psw"] == user.get_all[request.form["uname"]]: #check in database
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
        for i in user.get_all:
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

# @app.route("/home",methods=["GET","POST"])
# def home():
#     if request.method == "POST":

#     else:
#         return render_template("home.html")

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))

if __name__ == "__main__":
    user = User()
    app.run()   