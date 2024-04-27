from flask import Flask, request, redirect, session
from replit import db
import random
import os

app = Flask(__name__, static_url_path="/static")

currentUser = ""

app.secret_key = os.environ['sessionKey']


@app.route("/")
def index():
    if session.get('username'):
      return redirect("/welcome")
    else:
      page = ""
      f = open("templates/index.html", "r")
      page = f.read()
      f.close()
      return page


def checkUsernames(form):
    username = form["username"].lower()
    if username in list(db.keys()):
        print("Este usuario ya se encuentra registrado")
        return False
    else:
        print("Almacenando nuevo Usuario")
        salt = random.randint(1000000, 9999999)
        newPassword = f"{form['password']}{salt}"
        newPassword = hash(newPassword)
        db[username] = {
            "email": form["email"],
            "salt": salt,
            "password": newPassword
        }
        return True


@app.route('/setName', methods=["POST"])
def setName():
    if request.form['username'] == '':
      return redirect('/login')
    username = request.form['username']
    if username in list(db.keys()):
        password = request.form['password']
        salt = db[username]['salt']
        hashed_password = hash(f"{password}{salt}")
        if hashed_password == db[username]['password']:
            session['username'] = request.form['username']
            return redirect('welcome')
    else:
        print('no está en la lista')


@app.route("/welcome")
def welcome():
    page = ""
    currentUser = ""
    if session.get('username'):
        currentUser = session['username']
        f = open("templates/home.html", "r")
        page = f.read()
        f.close()
        page = page.replace("{currentUser}", currentUser)
        return page
    else:
        return redirect('/')


@app.route("/login", methods=["GET"])
def login():
    page = ""
    f = open("templates/login.html", "r")
    page = f.read()
    f.close()
    return page


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route("/delete-all")
def delete():
    for key in db.keys():
        del db[key]
    return redirect('/')


@app.route("/register", methods=["GET", "POST"])
def register():
    page = ""
    if request.method == "GET":
        f = open("templates/register.html")
        page = f.read()
        f.close()
        return page
    else:
        form = []
        form = request.form
        newUser = checkUsernames(form)
        if newUser:
            return redirect("/login")
        else:
            return redirect("/register")


app.run(host="0.0.0.0", port=81)
