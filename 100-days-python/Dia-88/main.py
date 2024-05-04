from flask import Flask, request, redirect, session
import datetime, os
from replit import db

app = Flask(__name__)
app.secret_key = os.environ["sessionKey"]


@app.route('/')
def index():
    page = ""
    f = open("templates/index.html", "r")
    page = f.read()
    posts_list = ""
    for key in db.keys():
        posts_list += f"""
      <div style="
        padding: 20px;
        border-radius: 10px;
        border: solid var(--text-100) 1px;
        margin: 10px;
      ">
          <h3>{db[key]['title']}</h3>
          <p>{db[key]['text']}</p>
        </div>
      """
    page = page.replace("{posts-list}", posts_list)
    f.close()
    return page


@app.route('/admin', methods=["GET", "POST"])
def admin():
  if not session.get("username"):
    print('no hay usuario, redirigir a login')
    return redirect('/login')
  else:
    if request.method == "GET":
      page = ''
      f = open("templates/admin.html", "r")
      page = f.read()
      posts_list = ""
      f.close()
      for key in db.keys():
        posts_list += f'<li style="list-style: none;font-size: larger;">{db[key]["title"]}</li>'
      page = page.replace("{posts-list}", posts_list)
      return page
      # if not session.get("username") and session['username'] != "borgesmj19":
      #   return redirect("/login")
      # else:
      #   if request.method == "GET":
      #       page = ''
      #       f = open("templates/admin.html", "r")
      #       page = f.read()
      #       posts_list = ""
      #       for key in db.keys():
      #           posts_list += f'<li style="list-style: none;font-size: larger;">{db[key]["title"]}</li>'
      #           print(db[key]['title'])
      #       page = page.replace("{posts-list}", posts_list)
      #       f.close()
      #       return page
      #   else:
      #       post_title = request.form['post-title']
      #       post_text = request.form['post-content']
      #       timestamp = round(datetime.datetime.now().timestamp())
      #       print(timestamp)
      #       db[timestamp] = {'text': post_text, 'title': post_title}
      #       return redirect('/admin')
        

@app.route('/login')
def login():
    page = ''
    f = open("templates/login.html", "r")
    page = f.read()
    userid = request.headers['X-Replit-User-Id']
    if userid == "31820613":
        session['username'] = request.headers['X-Replit-User-Name']
        print(session['username'])
        return redirect('/')
    return page


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(host='0.0.0.0', port=81)