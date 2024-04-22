# Demasiado código
Como quizas nos hemos dado cuenta, los archivos Flask se pueden volver grande muy rapido.

Nadie quiere todo ese código en una sola página, es demasiado.

HOy vamos a aprender como usar plantillas y redireccionar para adelgazar un poco las cosas.

👉 Aqui habrá un codigo flask simpl e para comenzar:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  myName = "David"
  page = f"""Hi {myName}"""
  return page

app.run(host='0.0.0.0', port=81)
```

👉 Esto esta bien para un codigo pequeño, pero para proyectos muchos mas largos pódemos crear **plantillas** para guardar nuestro HTML donde sea. Hagamoslo ahora:

1. Creemos una carpeta llamada **template**
2. Creemos un archivo HTML llamado **portfolio** dentro de la carpeta **template**

![download](download.png)

3. Ahora, vamos a pegar el cpódigo del portfolio de antes en la pagina portfolio
4. Ahora, crearemos una carpeta CSS y un archivo llamado **style.css**. Pegaremos el CSS del portfolio en ese archivo.
5. Editaremos el HTML para que tenga referencia al archivo CSS que acabamos de crear.
6. Aseguremosnos que todas las imagenes esten en subcarpetas aadecuadas. Edita todas las referencias en el portfolio.html para aseguarte que tenga los paths apropiados.

## Ahora de vuelta al main.py

1. Configura el fString a un string en blanco
2. Revisa un viejo amigo ` f = open()`
3. Abre el archivo `porfolio.html`
4. Lee el contenido dentro de la variable `page`

```python
@app.route('/')
def index():
  myName = "David"
  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  return page
```

## Mas páginas

Ahora, vemos a añadir una pagina 'home' al codigo Flask

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/home') # Creates the path to the home page
def home(): # Subroutine to create the home page
  # Three quotes followed by the html for the baldies site. Three more quotes to close. All the HTML is assigned to the 'page' variable
  page = """html

  <html>

  <head>
    <title>David's World Of Baldies</title>
  </head>


  <body>
  <h1>Dave's World of Baldies</h1> 
  <h2>Welcome to our website!</h2>

  <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

  <h2>Gallery of Baldies</h2>
  <p>Here are some of the legends of the bald world.</p>

  <img src="images/picard.jpg" width = 30%> 
  <p><a href = "https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>

  <ul>
    <li>Beautiful bald man</li>
    <li>Calm and cool under pressure</li>
    <li>All the Picard memes</li>
  </ul>

  <p><a href = "page2.html">Go to page 2</a></p>

</body>

</html>

  """

  return page # returns the contents of the page variable


app.run(host='0.0.0.0', port=81)
```

Ahora si visitamos la pagina *URL/home* en nuestro navegador, vamos a ser llevados a la pagina home.

# fString y reemplazos

USando fStrings y manipulacion de cadenas de caracteres `.replace()` de muchas lecciones atras nos deja personalizar la pagina web de nuestro usuario. Aqui veremos como:

👉 Primero, colocamos una placeholder por nombre en nuestro `portfolio.html`

```html
<body>

<h1>{name}'s Portfolio</h1>
```

Ahora, en el codigo Flask, podemos sar la funcion `.replace(). Notemos que se realiza antes del comando *return*

```python
@app.route('/')
def index():
  myName = "Katie"
  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{name}", myName) # Replace all instances of {name} with the contents of the 'myName' variable

  return page
```

Puedo usar esta tecnica para hacer multiples cambios a una pagina

:point_right: Veamos un codigo ejemplo, donde hemos creado una pagina generica que puede ser customizada por el usuario

```html
<body>

  <h1>{name}'s Portfolio</h1>
  <h2>{title}</h2>
  <p>{text}</p>
<a href="{link}"><img src="static/images/{image}" width="500px"></a>
```

:point_right: Ahora en el codigo `main.py` vamos a almacenar la informacion y usar multiples `replace`

```python
def index():
myName = "Katie"
title = "Day 56 Solution"
text = "So, day 56 was all about using csv reading and file and folder manipulation to make 100 files in dozens of folders. This was tricky because the names of the folders and files were based on the top 100 streaming songs and so weren't simple to encode."
image = "56.png"
link = "https://replit.com/@DavidAtReplit/Day-056-Solution#main.py"

page = ""
f = open("template/portfolio.html", "r")
page = f.read()
f.close()
page.replace("{name}", myName)
page.replace("{title}", title)
page.replace("{text}", text)
page.replace("{image}", image)
page.replace("{link}", link)
return page
```

HEmos recreado la misma pagina aqui, pero la hemos hecho de una manera que es **mas facil** usar la plantilla

:point_right: Por ejemplo, pudimos crear el Dia 56 como su propiar `app.route` asi:

```python
@app.route('/56')
def fiftySix():
  myName = "Dave"
  title = "Day 56 Solution"
  text = "So, day 56 was all about using csv reading and file and folder manipulation to make 100 files in dozens of folders. This was tricky because the names of the folders and files were based on the top 100 streaming songs and so weren't simple to encode."
  image = "56.png"
  link = "https://replit.com/@DavidAtReplit/Day-056-Solution#main.py"

  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  page.replace("{name}", myName)
  page.replace("{title}", title)
  page.replace("{text}", text)
  page.replace("{image}", image)
  page.replace("{link}", link)
  return page
```

Para crear el dia 57, solo escribire otra `app.route` con una subrutina, pero esta utilizará el archivo `portfolio.html` como plantilla. Solo necesito crear el archivo html una sola vez

### Intentalo :point_right:

## Redireccionar

Redireccionar es util cuando queremos enviar al usuario a otra direccion web, pero esa direccion es muy larga.

Esto requiere otro import al comienzo del archivo `main.py`:

```python
from flask import Flask, redirect
```

:point_right: Ahora añadiremos una `app.route`. En este ejemplo. queremos redireccionar a los usuarios al dia 77. Todo lo que hay qeu hacer es colocar en la subrutina `return redirect("")` con el URL dentro de las comillas.

```python
from flask import Flask, redirect

@app.route('/77')
def seventySeven():
  return redirect("https://replit.com/@DavidAtReplit/Day-077-Solution#main.py")

  return page
```

Esto es realmente podesoro. Efectivamente has creado tu propio acortador de links. Todo lo que el usuario debe hacer es añadir `/77` al final de la URL de la homepage.

# 👉 Desafío del día 77

El reto de hoy consiste en crear una plantilla sencilla para un blog.

Tu plantilla debe:

1. Tener un espacio para un encabezado
2. Tener un espacio para la fecha de hoy
3. Tenga un espacio para el texto.

- Ahora escriba dos entradas de blog diferentes y sírvalas en dos endpoints diferentes.
- Las entradas de blog deben utilizar la misma plantilla y tener redirecciones acortadas a sus URL.

Ejemplo:

![](recursos/06_reto1.png)
<detalles> <sumario> 💡 Consejos </sumario>

- No olvides `f= open()` y `f.read()` para obtener el HTML en python desde tu archivo de página trmplate.

</detalles>

