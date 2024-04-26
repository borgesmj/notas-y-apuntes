from flask import Flask, request, redirect
from replit import db
import random

app = Flask(__name__, static_url_path="/static")

currentUser = ""


@app.route("/")
def index():
    page = ""
    f = open("templates/index.html", "r")
    page = f.read()
    f.close()
    return page


def checkUsernames(form):
    username = form["username"]
    if username in list(db.keys()):
        print("Este usuario ya se encuentra registrado")
        return False
    else:
        print("Almacenando nuevo Usuario")
        salt = random.randint(1000000, 9999999)
        newPassword = f"{form['password']}{salt}"
        newPassword = hash(newPassword)
        db[username] = {"email": form["email"], "salt": salt, "password": newPassword}
        return True


@app.route("/welcome")
def welcome():
    global currentUser
    return f"Bienvenido {currentUser}"


@app.route("/login", methods=["GET", "POST"])
def login():
    global currentUser
    page = ""
    if request.method == "GET":
        f = open("templates/login.html", "r")
        page = f.read()
        f.close()
        return page
    else:
        username = request.form["username"]
        if username in list(db.keys()):
            salt = db[username]["salt"]
            newPassword = f"{request.form['password']}{salt}"
            newPassword = hash(newPassword)
            if newPassword != db[username]["password"]:
                print("Contraseña incorrecta")
                return redirect("/login")
            else:
                print("Usuario y contraseña correcto. redirigiendo...")
                currentUser = username
                return redirect("/welcome")
        else:
            print("Usuario no encontrado en la base de datos")
            return redirect("/login")


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
            return redirect("register")


app.run(host="0.0.0.0", port=81)
