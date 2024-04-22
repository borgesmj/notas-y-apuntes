from flask import Flask

reflections = [{'day': 77, 'text': "On this day, i build this website as a challenge. One day closer to the goal, reach the 100 days of python"}]

app = Flask(__name__)


@app.route('/')
def index():
    page = ""
    f = open("template/main.html", "r")
    page = f.read()
    f.close()
    return page


def setReflection(number):
    for item in reflections:
        if item['day'] == int(number):
            return item['text']
        return False


@app.route('/day-<pageNumber>')
def day(pageNumber):
    page = ""
    title = f"Day {pageNumber}"
    text = setReflection(pageNumber)
    print(text)
    if text == False:
      f = open("template/notfound.html")
      page = f.read()
      f.close()
      return page
    else:
      f = open("template/page.html", "r")
      page = f.read()
      f.close()
      page = page.replace("{title}", title)
      page = page.replace("{text}", text)
      return page


app.run(host='0.0.0.0', port=81)
