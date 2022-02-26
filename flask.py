from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)

@app.route("/",method=["GET","POST"])
def login():
    if request.method == "POST":
        #check user and password
        # if request.form["user"] == "student":
        
    else:
        return render_template("login.html")

@app.route("/home")

if __name__ == "__main__":
    app.run()   