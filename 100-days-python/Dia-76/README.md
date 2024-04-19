s# Flask!

La razon por la que hemos pasado los ultimos dias aprendiendo sobre HTML y CSS es para que podamos combianarlo con Python usando **Flask**

Flask nos permite construit nuestro propio servir web. Esto significa que corre todo el tiempo, creando las paginas donde entremos en nuestro website.

La razon por la que Flask es diferente de solo usar HTML y CSS es que podemos construir web apps dinamicas que puedan camiar dependiendo del usuario

Un servidor web funciona un poco diferente. Ya nosotros hemos creado un servidor web, click en `run` y dale la direccion del sitio web a cualquiera que quiera usar el programa. Esto significa que podemos hacer nuestro codigo privado si queremos.

## ¿Como el codigo Flask es distinto?

Vamos a meternos un poco mas en el codigo propporcionado, y veamos los comentarios para explicaciones:

```python
from flask import Flask # Imports the flask library

app = Flask(__name__) # Starts the Flask application. The 'app' variable is very important. We'll be using that later.


@app.route('/') # Tells the code what to do if we've gone to our web address with just a / after the URL
def index(): # Tells the code which webpage to show. This subroutine will display the 'Hello from Flask' page
    return 'Hello from Flask!'



app.run(host='0.0.0.0', port=81) # This line should ALWAYS come last. It's the line that turns on the Flask server.
```

Cuando corremos este codigo iniciador, esta es la pagina que nos regresa:

![image](https://github.com/borgesmj/notas-y-apuntes/assets/121818423/5f7f60ee-629d-42a8-823d-b1841f2d10d0)


Puedes ves que la URL de la pagina en la parte de arriba del screenshot. Puedes visitar la pagina la misma URL dessde tu tlf o tablet y veras la misma pagina.

## Mas paginas

Ahora, vamos a añadir la pagina 'about' al codigo Flask.

```python
from flask import Flask # Imports the flask library

app = Flask(__name__) # Starts the Flask application. The 'app' variable is very important. We'll be using that later.


@app.route('/') # Tells the code what to do if we've gone to our web address with just a / after the URL
def index(): # Tells the code which webpage to show. This subroutine will display the 'Hello from Flask' page
    return 'Hello from Flask!'

@app.route('/about/')
def about():
  page = """<html>

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
  return page


app.run(host='0.0.0.0', port=81) # This line should ALWAYS come last. It's the line that turns on the Flask server.
```

Ahora si visitamos la pagina URL/*about* en nuestro navegador, seremos llevados a la pagina `about` para ver la obra maestra qeu hemos creado.

Puedes notar que la imagen no se ve, eso es algo que solucionaremos ahora.

## Imagenes com Flask

Para obtener imagenes con Flask, debemos:

1. Crear una carpeta en el panel de archivos. POr defecto, debe llamarse 'static'
2. Carga cualquier archivo que quieras que la pagina web tenga acceso, imagenes, audio, video, etc. Puees crear subcarpetas para mantenerte mas organizado.
3. Añade una nueva propiedad a la linea de codigo `app = Flask`
```python
app = Flask(__name__, static_url_path="/static")
```

Hemos añadido una subcarpeta 'images' y cargamos una imagen allí.


![download](download_2.png)

Ahora, actualizamos la etiqueta `<img>` para hacer referencia a la carpeta 'static'.

```html
<img src="/images/picard.jpg" width = 30%> 
<!-- los .. es para que la ruta a la imagen sea para la main -->
```

## Inténtalo

# fStrings con Flask

Una de las cosas cool que podemos usar con Flask son fString para formatear contenido dentro de nuestra pagina web.

Digamos que queremos insertar la fecha de hoy en la pagina inicial. Yo debo:

1. Escribir el codigo para obtener la fecha dentro de la subrutina `about` y asignarlo a una variable.
2. Formatear el HTML con un fString
3. Usa los corchetes para colocar la variable de la fecha en el HTML.

Aqui está el codigo:

```python
from flask import Flask
import datetime # Importamos la libreria

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/about/')
def about():
  today = datetime.date.today() # GEt the today's date
  page = f"""<html>

    <head>
      <title>David's World Of Baldies</title>
    </head>
    <body>
    <h1>Dave's World of Baldies</h1> 
    <h2>Welcome to our website!</h2>
    <h2>Today's date is: {today}</h2> # Colocamos la fecha
    <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>
    <h2>Gallery of Baldies</h2>
    <p>Here are some of the legends of the bald world.</p>
    <img src="../static/images/picard.jpg" width = 30%> 
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
  return page


app.run(host='0.0.0.0', port=81)
```

## Enlazando con Flask

Vamos a añadir un link desde nuestro index a nuesra pagina 'about'. Vamos a mostrar el pezado de codigo que pertenece al `index` para añadir algun contenido rapido con un link.

```python
@app.route('/')
def index():
  page = f"""<html><body>
  <p><a href = "/about/">Go about</a></p>
  </body>
  </html>"""

  return page
```

## Inténtalo

## Errores comunes

### Copy, paste and edit

👉 ¿Cual es el problema aqui?

```python
from flask import Flask
import datetime

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index(): 
  page = f"""<html><body>
  <p><a href = "/home">Go home</a></p>
  </body>
  </html>"""
  return page

@app.route('/home') 
def index(): 
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

  return page


app.run(host='0.0.0.0', port=81)
```
El problema es que hay dos paginas distintas `/`y `/home` que ambas tienen la misma subrutina `index()`

## Sin direccion

👉 ¿Cual es el problema aqui?

```python
from flask import Flask
import datetime # import the datetime library

app = Flask(__name__)
```

Cuando queremos cargar imagenes desde nuestro servidor, debemos agregar la ruta de la carpeta a la variable `app`

```python
from flask import Flask
import datetime

app = Flask(__name__, static_url_path="/static")
```

## 👉 Reto del dia 76

El reto de hoy es crear un servidor web Flask con dos endpoint.

Nuestro programa debe:
1. Tener un `/portfolio` que despliegue la oagina de portfolio
2. Tener un `/linktree` que despliegue nuestro linktree page.

Consejos:

+ Asegúrese de tener una carpeta "estática" para todos sus archivos multimedia y CSS.
+ Es posible que tengas que cambiar el nombre de un archivo CSS para evitar tener dos con el mismo nombre.
