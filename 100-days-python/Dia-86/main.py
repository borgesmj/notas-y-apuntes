from flask import Flask, redirect, session, request
import os, random, datetime
from replit import db

app = Flask(__name__)
app.secret_key = os.environ["sessionKey"]


def find_user(username):
    usernames_list = []
    try:
        for row in list(db["users"]):
            usernames_list.append(row["username"])
    except:
        pass
    if username in usernames_list:
        return True


def get_user_data(username):
    data = []
    for row in list(db["users"]):
        if row["username"] == username:
            data = row
            return data


@app.route("/delete_all")
def delete():
    for key in db.keys():
        del db[key]
    return redirect("/")


@app.route("/success")
def success():
    page = ''
    f = open("templates/sucess.html", "r")
    page = f.read()
    f.close()
    return page


def getAll_posts():
    all_posts = []
    try:
        for row in db['posts']:
            all_posts.append(row)
    except:
        pass
    return all_posts


@app.route("/post", methods=["POST"])
def post():
    if request.method == "POST":
        all_posts = getAll_posts()
        new_post = {
            'text': str(request.form['post']),
            'user': str(session.get('username')),
            'date': str(datetime.datetime.now())
        }
        all_posts.append(new_post)
        db['posts'] = all_posts
        print('desde /post')
        print(all_posts)
        return redirect('/home')


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        page = ""
        f = open("templates/register.html", "r")
        page = f.read()
        f.close()
        return page
    else:
        userExists = find_user(request.form['username'])
        if not userExists:
            usersData = []
            salt = random.randint(1000000, 9999999)
            hashed_password = hash(f"{request.form['password']}{salt}")
            usersData.append({
                'fullname': request.form['fullname'],
                'username': request.form['username'].lower(),
                'password': hashed_password,
                'salt': salt
            })
            db['users'] = usersData
            return redirect('/success')
        else:
            return redirect('/register')


@app.route("/home")
def home():
    all_posts = []
    all_posts = getAll_posts()
    username = session.get("username")
    page = ''
    with open("templates/home.html", "r") as f:
        page = f.read()
    posts_list = ""
    page = page.replace("{username}", username)
    for post in all_posts:
        posts_list += f"""
      <li style='list-style: none; padding: 10px; display: flex; flex-direction: column; border: 2px solid black; border-radius: 10px; margin-block: 10px;'>
            <span>by: {post['user']}</span>
            <p style='font-weight: bold;font-size: 30px;'>{post['text']}</p>
            <span>at: {post['date']}</span>
      </li>"""
    page = page.replace("{posts_list}", posts_list)
    return page


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route("/")
def index():
    if session.get("username"):
        return redirect("/home")
    else:
        return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        page = ""
        f = open("templates/login.html", "r")
        page = f.read()
        return page
    else:
        username = request.form['username'].lower()
        userExists = find_user(username)
        if not userExists:
            return redirect('/register')
        else:
            userdata = get_user_data(username)
            hashed_password = hash(
                f"{request.form['password']}{userdata['salt']}")
            if userdata['password'] == hashed_password:
                session['username'] = userdata['username']
                return redirect('/home')
            else:
                return redirect('/login')


app.run(host="0.0.0.0", port=81)
