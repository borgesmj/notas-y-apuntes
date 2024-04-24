¡# Incoming!

Hoy vamos a aprender a manejar datos de formularios en Flask.

👉 Para empezar, ya he añadido el código HTML de ayer para mi formulario en `main.py`. (¡De nada!) ¡Ve a echarle un vistazo!
##
👉 Sin embargo, de momento, la `@app.route()` no tiene ningún método asociado, así que necesito crear una ruta para que esta página reciba los datos.

En primer lugar, necesito un nuevo import: `request`.

Luego creo el `@app.route` - también necesito añadir un argumento extra para especificar los métodos que se reciben. Por el momento, es sólo 'post', pero **tiene** que ser **ALL CAPS** - `POST`.

Finalmente defino la subrutina `process()` que devuelve `request.form`.

👉 Aquí está el nuevo código solo:

```python
from Flask import Flask, request

@app.route('/process', methods=["POST"])

def process():
  return request.form
```

👉 Y aquí está como parte del código completo:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/process", methods=["POST"])

def process():
  return request.form

  
@app.route('/')
def index():
  page = """<form method = "post" action="/process">
    <p>Name: <input type="text" name="username" required> </p>
    <p>Email: <input type="Email" name="email"> </p>
    <p>Website: <input type="url" name="website"> </p>
    <p>Age: <input type="number" name="age"> </p>
    <input type="hidden" name="userID" value="232"> </p>

    <p>
      Fave Baldy: 
      <select name="baldies">
        <option>David</option>
        <option>Jean Luc Picard</option>
        <option>Yul Brynner</option>
      </select>
    </p>

    <button type="submit">Save Data</button>
  </form>
    
    
    """
  return page
app.run(host='0.0.0.0', port=81)
```


This will get us the data from the form in a dictionary format, like this:

![](resources/01_post1.png)
##
👉 Ahora puedo empezar a añadir a la subrutina `process()` y usar sentencias `if` para decidir qué vamos a decir dependiendo de los datos recibidos. Esto es lo que he hecho en el siguiente ejemplo:
1. Configurar una variable llamada `página` en blanco, y otra llamada `formulario` y asignarle los datos entrantes del formulario.
2. Usar selección para comprobar si el usuario eligió 'david' como su calvo favorito. `page +=` significa *añadir a la página*.
3. Añadir un mensaje de felicitación personalizado con el nombre del usuario (he usado comillas simples en el fString para pasar el posible problema de que ya he usado dobles antes en mi código).
4. Añadido un `else` para aquellos que eligieron.... imprudentemente.

```python
def process():
  page = ""
  form = request.form

  if form["baldies"] == "david":
    page += f"You're alright {form['username']}"
  else:
    page += f"You've picked wrong {form['username']}"

  return page
```
### ¡Pruébalo!

# 👉 Desafío del Día 80

Ve y coge el código de tu formulario de acceso de ayer. 

Conéctalo a Flask.

Haz que funcione.

Debería haber:

1. Tres combinaciones válidas de nombre de usuario y contraseña.
2. Una página 'agradable' para usuarios válidos.
3. 3. Una horrible página "traviesa" para usuarios no válidos/intentos de pirateo.
    
Ejemplo:

![](resources/04_challenge1.png)

![](resources/04_challenge2.png)
<detalles> <sumario> 💡 Pistas </sumario>
  
- Utiliza un diccionario para almacenar los nombres de usuario y contraseñas válidos.
- Utilice una variable booleana para almacenar si una combinación válida está presente en el diccionario o no.
- Utiliza `try .... except` para iniciar sesión.

</detalles>