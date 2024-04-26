from flask import Flask, redirect, request

app = Flask(__name__, static_url_path="/static")


@app.route("/", methods=["GET"])
def index():
    themes = [
        "<body>",
        '<body class="theme-default">',
        '<body class="there-ligth">',
        '<body class="theme-dark">',
    ]
    myName = "Miguel"
    f = open("template/main.html", "r")
    page = ""
    page = f.read()
    f.close()
    page = page.replace("{name}", myName)
    args = request.args
    currentTheme = ""
    className = ""
    for text in themes:
        if text in page:
            currentTheme = text
    if "theme" in args:
        newTheme = f"theme-{args['theme']}"
        page = page.replace(currentTheme, f'<body class="{newTheme}">')
    else:
        print("no hay parametros")
        page = page.replace(currentTheme, "<body>")
    return page


@app.route("/entry-1")
def first_entry():
    title = "Replit DB"
    text = "This is the challenge for day 61 of #100DaysPython, this day we learn about storage data inside the replit DB"
    link = "https://github.com/borgesmj/notas-y-apuntes/blob/main/100-days-python/Dia-61/README.md"
    page = ""
    f = open("template/entryTemplate.html")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    page = page.replace("{text}", text)
    page = page.replace("{link}", link)
    return page


@app.route("/entry-2")
def second_entry():
    title = "Comma-Separated Values"
    text = "This is the challenge for day 54 of #100DaysPython, this day we learn about storage data inside a comma separated values file"
    link = "https://github.com/borgesmj/notas-y-apuntes/blob/main/100-days-python/Dia-54/README.md"
    page = ""
    f = open("template/entryTemplate.html")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    page = page.replace("{text}", text)
    page = page.replace("{link}", link)
    return page


app.run(host="0.0.0.0", port=81)
