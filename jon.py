from flask  import Flask
from flask import render_template

app = Flask (__name__) 
 
@app.route("/login/")
def login():
    return render_template('login.html')

@app.route("/register/")
def register():
    return render_template('register.html')

@app.route("/logout/")
def logout():
    return render_template('logout.html')