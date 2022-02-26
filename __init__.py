from flask import Flask,render_template,redirect,url_for,request,session

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        error = "User not found"
        #check user and password
        if request.form["uname"] in : #check in database
            error = "Incorrect Password"
            if request.form["psw"] in : #check in database
                session['username'] = request.form["uname"]
                return redirect(url_for('home'))
        return render_template("login.html",error=error)
    # else:
    return render_template("login.html",error="None")

@app.route("/registration",methods=["GET","POST"])
def registration():
    if request.method == "POST":
        if request.form["uname"] in #check exisiting or not
            error = "username already exists"
            return render_template("register.html",error="None")
        else:
            #write into database
            request.form["uname"]
            request.form["psw"]
            request.form["fullname"]
            request.form["loca"]
            request.form["salary"]
            request.form["interest"]
            return redirect(url_for('login'))
        #register user credentials
    else:
        return render_template("register.html",error="None")

# @app.route("/home",methods=["GET","POST"])
# def home():
#     if request.method == "POST":
#     else:
#         return render_template("home.html")

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()   