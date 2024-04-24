from flask import Flask, request

app = Flask(__name__)


@app.route('/language', methods=["GET"])
def language():
  data = request.args['lang']
  if data.lower() == 'eng':
    return "<h1>Welcome to our small litle world</h1>"
  elif data.lower() == 'esp':
      return "<h1>Bienvenido a nuestro pequeño mundo</h1>"
  elif data.lower() == 'dut':
    return "<h1>Willkommen in unserer kleinen, feinen Welt</h1>"
  elif data.lower() == 'jap':
    return "<h1>小さな小さな世界へようこそ</h1>"

  return "<p>Nothing to see here</p>"


@app.route("/")
def index():
  return """
        <ul>
          <li>
            <a href="./language?lang=eng">English</a>
          </li>
          <li>
            <a href="./language?lang=esp">Español</a>
          </li>
          <li>
            <a href="./language?lang=dut">Dutch</a>
          </li>
          <li>
            <a href="./language?lang=jap">Japanese</a>
          </li>
        </ul>
        """
app.run(host='0.0.0.0', port=81)