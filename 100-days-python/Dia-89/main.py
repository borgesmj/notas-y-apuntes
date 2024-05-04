from flask import Flask, request, session, redirect, Response
import os, datetime
from replit import db

app = Flask(__name__)
app.secret_key = os.environ["sessionKey"]


def build_messages():
    messages = ""
    keys = db.keys()
    keys = list(keys)
    for key in reversed(keys):
        message = ""
        f = open("templates/message.html", "r")
        message = f.read()
        message = message.replace("{Autor}", db[key]['author'])
        message = message.replace("{Este es un mensaje}", db[key]['message'])
        message = message.replace("{date}", db[key]['date'])
        if session.get('username') == db[key]['author']:
            message = message.replace("{left-rigth}", "justify-self: flex-end")
            message = message.replace("{background-color}", "background-color: #05db24")
        else:
            message = message.replace("{left-rigth}", "justify-self: flex-start")
            message = message.replace("{background-color}", "background-color: #db7005")
        messages += message
    return messages


@app.route('/')
def index():
    if 'username' in session:
        page = ""
        username = session['username']
        f = open("templates/index.html", "r")
        page = f.read()
        f.close()
        print(session)
        page = page.replace("{username}", username)
        messages = build_messages()
        page = page.replace("{messages}", messages)
        return page
    else:
        return redirect('/login')


@app.route("/post", methods=["POST"])
def post():
    date = datetime.datetime.now()
    timestamp = round(datetime.datetime.now().timestamp())
    username = session['username']
    db[timestamp] = {
        'date': str(date),
        'message': request.form['message'],
        'author': username
    }
    # Envía un evento SSE para notificar a los clientes sobre el nuevo mensaje
    send_event_to_clients("Nuevo mensaje publicado")
    return redirect("/")


@app.route('/login')
def login():
    print(session)
    if 'username' not in session:
        page = ""
        f = open("templates/login.html", "r")
        page = f.read()
        f.close()
        session['id'] = request.headers['X-Replit-User-Id']
        session['username'] = request.headers['X-Replit-User-Name']
        return page
    else:
        return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    print(session)
    return redirect("/")


@app.route("/delete")
def delete():
    for key in db.keys():
        del db[key]
    return redirect("/logout")


def send_event_to_clients(event_data):
    for client in clients:
        client.send(event_data)


clients = set()


@app.route('/stream')
def stream():
    def event_stream():
        client = request.environ.get('wsgi.websocket')
        clients.add(client)
        while True:
            # Espera indefinidamente nuevos mensajes, no es necesario enviar eventos aquí
            message = client.receive()
            yield message

    return Response(event_stream(), content_type='text/event-stream')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
