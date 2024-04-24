from flask import Flask, request, redirect, url_for

app = Flask(__name__)

logins = {}
logins['borgesmj'] = {'email': 'borgesmj@correo.com', 'password': '123456'}
logins['samantha'] = {'email': 'samantha@correo.com', 'password': '654321'}
logins['arismer'] = {'email': 'arismer@correo.com', 'password': '000000'}

currentUser = ''
@app.route("/login", methods=["POST"])
def login():
  global currentUser
  form = request.form
  try:
    details = logins[form['username']]
  except:
    return redirect(url_for('index'))
  currentUser = form['username']
  if details['password'] == form['password'] and details['email'] == form['email']:
    return redirect(url_for('userProfile'))
  else:
    return redirect(url_for('index'))

@app.route("/profile")
def userProfile():
  global currentUser
  page = ""
  f = open("login.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{username}", currentUser)
  return page

@app.route('/')
def index():
    page = ""
    f = open("main.html", "r")
    page = f.read()
    f.close()
    return page

app.run(host='0.0.0.0', port=8080)
