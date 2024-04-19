from flask import Flask

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
  return """
  <a href='/portfolio'>Portfolio</a>
  """

@app.route('/portfolio')
def portfolio():
    return """
  <!DOCTYPE html>
  <html>

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Miguel's replit</title>
    <link href="static/styles/portfolio.css" rel="stylesheet" type="text/css" />
  </head>

  <body>
    <div id="root"></div>
    <script src="static/scripts/portfolio.js"></script>
    <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script> 
  </body>

  </html>
  """


app.run(host='0.0.0.0', port=81)
