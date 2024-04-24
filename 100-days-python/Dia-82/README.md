# No te detengas hasta que lo tengas

Hoy vamos a aprender acerca una manera alternativa de obtener data desde formularios del servidor web.

Hasta ahora, hemos usado `post`, que (mas o menos) empaqueta toda la data desde el formulario y lo envia al servidor.

Cuando pensamos en esto como la manera de controlar cuando la data es enviada.

Con el metodo `get`, la solicitud para la data viene **desde el servidor web**. Eso efectivamente dice "dame esa data" para el formulario.

Practicamente hemos visto `get`en uso antes. Si antes has visto alguna URL con un `?` despues del nombre de la website, estonces un monton de `=` y quizas simbolos como `&`, entonces esa website está usando `get`.

## Entonces. ¿cual es la diferencia?

Me alegra que preguntes.

Con `post` la data en el formulario no puede ser vista en el navegador web. Una vez que se envia, se fué. Esto quiere decir qu no podemos marcar, guardar o compartir la data de una URL basada en `post`porque será distinta para cada usuario. ¿Alguna vez has querido compartir el link de un carrito de compras? Solo para obtener que ese link no lleva a ningun lado. Eso es el problema con post, el link será distinto para ti que para otros usuarios.

Obtener (`get`) data codifica la data de una URL, asi qeu lo podemos marcar y compartirlo y obtendremos los mismos resultados.

:point_right: Añadamos un poco mas de codigo a nuestro programa Flask para mostrar como funciona:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
  return 'Hello from Flask'

app.run(host='0.0.0.0', port=81)
```

:point_right: Correr este codigo con `get` funcionará. Mientras que si hubiesemos hecho lo mismo con `post`, eso causará un error.

## Solicitud de importacion

:point_right: De nuevo, tratamos de importar `request` y cambiar el return to `return request.args`

Esto va a retornar cualquier argumento codificado en la URL

```python
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
  return request.args

app.run(host='0.0.0.0', port=81)
```

Correr este codigo nos traerá este output (un dicctionario vacio), porque al momento no hay argumentos codificados en la URL.

![download](download.png)

:point_right: Mira la página en el navegadpr y añade una variable o dos al final de la uRL asi:

![download](download_2.png)

Presiona enter y mira que pasa:

![download](download_3.png)

Estamos construyendo un diccionario pasando variables en la URL.

## Personalizacion

Si configuramos nuestro codigo Flask para que nuestro `request.args` es asignada a una variable `get`, entonces podemos usar alguna seleccion para hacer una personalizacion cool.

```python
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
  get = request.args
  if get["name"].lower() == "david":
    return "Hello baldie"

app.run(host='0.0.0.0', port=81)
```

Mira lo que esto hace en el navegador.

![download](download_4.png)

## Return 'no data'

:point_right: Tambien necesitamos una linea `return "no data"`si no hay data presente.

```python
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
  get = request.args
  if get["name"].lower() == "david":
    return "Hello baldie"

  return "No data"

app.run(host='0.0.0.0', port=81)
```

La razon para ese `return "no data"` no está dentro de un `else` es por la manera que `return` funciona.

Cuando una subrutina encuentra un `return`, lo saca de la subrutina,asi que si tu nombre es 'david', entonces la subrutina regresará "hello baldie" y se saldra, de lo contrario va a ir al `return "no data"`

## ¿Deberia usar Post o Get?

Con `post`, la data trasmitida es encriptada usando el metodo de la webpage por defecto. Asi que si la URL comienza con `https`, entonces esencriptada usando el algoritmo de cifrado de protocolo seguro de transferencia de hypertexto.


Esto hace de `post`una mejor opcion para nombres de usuarios, contraseñas, etc.

Con `get`, la data es enviada como texto plano como pate de la URL, asi que no es bueo para la data que quieras que este segura. Sin embargo, es util para configuracioes, locaciones u otras cosas que quieras que este disponible en la url guardada.

# Reto 👉 Día 82

El reto de hoy es ¡hacerte bilingüe!

1. Escribe una página en inglés con una terminación `/language` en la URL.
2. La página de carga por defecto debe ser esta página en inglés.
3. Crea una página duplicada en otro idioma (¡hola Google translate!).
4. Utiliza la variable get para comprobar la URL en qué idioma mostrarla.
5. Si la URL termina en `/english`, entonces muestra la página en inglés.
6. Si termina en `/otherLanguage`, entonces muestra tu página traducida en su lugar.



<detalles> <sumario> 💡 Consejos </sumario>

- Utilice datos == {} para comprobar si hay una página vacía.

</detalles>


La solucion la tenemos en [main.py](./main.py)