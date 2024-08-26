import os
from flask import Flask, send_file, request
from fetchData import fetchTracks
app = Flask(__name__)

@app.route("/", methods=["POST"])
def changeYear():
    year = request.form.get("year")
    songsList = fetchTracks(year)
    f = open("src/index.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{year}", year)
    page = page.replace("Introduce un año y te regresará el top 10 de música de ese año", f"Este es el top list del {year}")
    page = page.replace("{songsList}", songsList)
    return page

@app.route("/")
def index():
    f = open("src/index.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{songsList}", "Introduce un año")
    return page

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
