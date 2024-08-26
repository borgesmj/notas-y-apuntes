# ¿API? ¿Spotify? Verifica.

Las API que hemos estado usando hasta ahora son bastante inusuales en que proporcionan su servicio de forma gratuita.

Normalmente, tienes que pagar para usar un servicio de datos de APIs (al menos si lo estás haciendo comercialmente). Esto significa que tendrás que verificar tu estado como usuario aprobado antes de que puedas conseguir tus manos sucias en todos esos dulces datos.

Hoy, estamos aprendiendo a escribir un programa que le dice a una API que tenemos una cuenta antes de acceder a su información.

No te preocupes, no tendrás que sacar la tarjeta de crédito. Estamos usando una API de Spotify que no cobrará siempre que mantengamos nuestro uso bajo un cierto nivel.

Nota: Spotify ha reservado esta API para aplicaciones de nivel de producción. Para asegurarnos de que podemos seguir utilizando la API para aprender y construir en 100DoC, le pedimos que por favor se abstenga de solicitar extensiones de cuotas de Spotify para sus proyectos de 100DoC.

## Empecemos

:point_right: [Haga clic aquí para ir a la página de desarrollador](https://developer.spotify.com/dashboard) de Spotify e inicie sesión/crear una cuenta.

:point_right: A continuación, pulse, crear una aplicación y darle un nombre y una descripción.


Copie el **CLIENT_ID** e inserte como un secreto en su REPL. Asegúrese de llamarlo CLIENT_ID.

## Client secret

Volver a Spotify y haga clic en mostrar el secreto del cliente (utiliza el tuyo, no el de estas capturas de pantalla, lo habré cambiado para el momento en que esto salga). Una vez más, copiar y crear un secreto REPL para ello como **CLIENT_SECRET**.

Ahora tenemos, efectivamente, el nombre de usuario y la contraseña que nuestro programa necesita para que pueda hablar con Spotify.

## Autenticacion

Ahora tenemos acceso a un montón de datos relacionados con la música. Puede encontrar y probar todos los datos de diferentes categorías en la página de API de spotify en la pestaña de categorías.

## Conéctate a Spotify

Primero, sin embargo, necesitamos conectar nuestro programa con Spotify. 
  1. El paso 1 es importar un montón de bibliotecas. La línea 2 es una nueva biblioteca que autentica nuestras credenciales de Spotify contra su API.

```python
import requests, json, os
from requests.auth import HTTPBasicAuth
```

  2. A continuación, traer nuestros secretos y asignar a las variables.

```python
import requests, json, os
from requests.auth import HTTPBasicAuth

clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']
```
## Autenticate

:point_right: Ahora a autenticar con el sistema de Spotify. Esta es complicada la primera vez, pero después de eso tendrás el código que puedes reutilizar.

_Authenticating_ le da una token (una serie de números y letras aparentemente aleatorios) que es el pase de 'Estoy permitido aquí' para tu programa.

Aquí pasa mucho. Así que, aquí está la ruptura:

  * He configurado variables para almacenar los datos necesarios para la autenticación.
    - `url` almacena la dirección web a la que conectarse
    - `data` crea un diccionario que se comunica con la API de la manera correcta. Básicamente le dice a Spotify 'Envíeme de nuevo las credenciales basadas en mi identificación de cliente y secreto. Aquí hay un formato de diccionario para ponerlos.
    - `auth` utiliza la nueva función `HTTPBasicAuth` para enviar su ID de cliente y secreto a Spotify como más o menos el nombre de usuario y contraseña para iniciar sesión.
    - `response` almacena la clave de la API que será devuelta por la función  `request` que envía a Spotify la información de inicio de sesión necesaria.
    Después de eso, he añadido algunas funciones de impresión a la salida de la información que rectamos para propósitos de prueba.

```python
url = "https://accounts.spotify.com/api/token"
data = {"grant_type":"client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)

response = requests.post(url, data=data, auth=auth)

print(response.ok)
print(response.json())
print(response.status_code)
```

nos regresa unos valores asi:

```
True
{'access_token': 'BQAw56u5yri3ylqX0cAPG-iPc1vTVFSWExG3xKj8KmYuz9-zzkvT089Pl-Nov4n4atU2hwoJuYqUrX4QH68mCmzFNVu-szSX6UTwuegwzohoQg3iSPs', 'token_type': 'Bearer', 'expires_in': 3600}
200

```
## Código entero hasta ahora

Una vez que haya probado las huellas y sé que todo está funcionando, puedo quitarlas y extraer el token. Este es el código hasta ahora:

```python
import requests, json, os
from requests.auth import HTTPBasicAuth

clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

url = "https://accounts.spotify.com/api/token"
data = {"grant_type":"client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)

response = requests.post(url, data=data, auth=auth)
accessToken = response.json()["access_token"]
```
## Configura una busqueda

Ahora vamos a configurar un formulario de búsqueda Spotify. He ido a [la página de la API](https://developer.spotify.com/documentation/web-api), he seleccionado la consola y he tomado los detalles del endpoint.

Lo he insertado en mi repl en la variable url (puedo reutilizarlo porque ha hecho su trabajo de logging anteriormente). Además, he establecido una variable de `headers` que permitirá la comunicación con la API de Spotify usando mi token de acceso como un pase.

```python
url = "https://api.spotify.com/v1/search"
headers = {'Authorization': f'Bearer {accessToken}'}
```

## Token de acceso

- Volver a Spotify ahora, y vamos a buscar a un artista. Copie su token de acceso (es posible que tenga que imprimirlo de nuevo) y pegarlo en la caja OAuthToken en Spotify. A continuación, haga clic en solicitar.

Rellenar los detalles

Ahora rellene el resto de los detalles en el menú de búsqueda de Spotify. Usted puede ver muchos ejemplos de lo que buscar en la página de referencia de la API. A continuación, haga clic en Inténtalo y desplácese hacia abajo para ver el JSON a la derecha de la pantalla.

## Coge parte de la consulta

A continuación voy a agarrar parte de la consulta de la página de Spotify y llevarla a una variable en mi Repl. La parte que he agarrado especifica que estoy buscando pistas de 'Queen', y sólo quiero mostrar 5 resultados.

```
search = "?q=artist%3Aqueen&type=track&limit=5"
```

## La consulta completa

A continuación, cree la consulta completa concatenando las variables de url y búsqueda. He incluido el código completo aquí. La nueva línea es la última.

```python
import requests, json, os
from requests.auth import HTTPBasicAuth

clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

url = "https://accounts.spotify.com/api/token"
data = {"grant_type":"client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)

response = requests.post(url, data=data, auth=auth)

accessToken = response.json()["access_token"]

url = "https://api.spotify.com/v1/search"
headers = {'Authorization': f'Bearer {accessToken}'}
search = "?q=artist%3Aqueen&type=track&limit=5"

fullURL = f"{url}{search}"
```

- Por fin. Es hora de enviar esa url y obtener algunos resultados de ella. También necesito enviar a los `headers` para obtener autorización.

```python
response = requests.get(fullUrl, headers=headers)

data = response.json()

print(json.dumps(data, indent=2)) 
```

También he usado un bucle para despojar sólo los nombres de la pista y sacarlos.

```python
for track in data["tracks"]["items"]:
print(track["name"])
```
## Vista previa de la canción

Spotify también incluye una URL de vista previa - una muestra de 30 segundos de la canción, así que he añadido un enlace a esa muestra como parte de la salida.

```python
response = requests.get(fullURL, headers=headers)

for track in data["tracks"]["items"]:
  print(track["name"])
  print(track["preview_url"])
```
## Haciéndola de este personalizable

En lo que cómo hacer personalizable nuestro usuario de búsqueda? En el siguiente código, tengo:

* Pregunté al usuario que ingresara a un artista
* Sucedió su entrada
* formateé la URL de búsqueda como un fString que incluye al artista

Aquí está el código:

