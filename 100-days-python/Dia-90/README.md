# JSON

Es el día 90, y hoy vamos a empezar a aprender a utilizar **JSON** (java script object notation - pronunciado Jason) para obtener datos de otros sitios web. Es el primer paso en nuestro viaje hacia el web scraping.

JSON es una forma basada en texto de describir el aspecto de un diccionario 2D. Esto es importante a la hora de enviar mensajes a otros sitios web y obtener un mensaje de vuelta y decodificarlo. La mayoría de las veces, el mensaje que recibimos de vuelta estará en formato JSON, y necesitamos interpretarlo en Python como un diccionario 2D para darle sentido.

## Ve a Get Data

👉 Vamos a hacer una simple captura de datos de un sitio web de uso gratuito - *randomuser.me* que genera algunos datos sobre un usuario ficticio.
```python
import requests # import the required library

result = requests.get("https://randomuser.me/api/") # ask the site for data and store it in a variable

print(result.json()) # interpret the data in the variable as json and print it.
```
Ejecútalo. Obtendrás **muchos** datos.

## Ordénalo
👉 A continuación, vamos a intentar ordenarlo un poco.

```python
import requests, json #imports the json library

result = requests.get("https://randomuser.me/api/")
user = result.json() #a dictionary containing the user's data
print(json.dumps(user, indent=2)) #outputs the json to the console with an indent to make it more readable.
```
Esto debería formatear tu salida un poco mejor, y deberías ser capaz de ver que efectivamente está en formato diccionario. El diccionario de primer nivel se llama `results`.

![](recursos/01-json1.png)

## Salida
👉 Este es el código para dar salida a un dato sobre el usuario. Voy a mostrar su nombre y apellidos.  He comentado la línea de código 'output everything' para centrarme en la información de salida.


``python
import requests, json 

result = requests.get("https://randomuser.me/api/")
user = result.json() 
# print(json.dumps(user, indent=2)) 

name = f"""{user["results"][0]["name"]["first"]} {user["results"][0]["name"]["last"]}""" # Get the first and last names from the results dictionary and assign to a variable

print(name) # output the variable
```
Cada vez que ejecutes el código, debería obtener un nuevo usuario aleatorio del sitio y mostrar su nombre.

## Imágenes, todo el mundo necesita buenas imágenes


Si te has desplazado por el gran archivo de datos json, te habrás dado cuenta de que las imágenes también forman parte del perfil de nuestro usuario aleatorio:
![](recursos/01-json2.png)

👉 Obtengamos también la imagen y almacenémosla en un archivo local. Aquí está el código aislado:

``python
image = f"""{user["results"][0]["picture"]["medium"]}""" # Get the user's profile picture and assign to a variable, changing 'medium' to 'large' will make the image less pixelated
picture = requests.get(image) #downloads the image
f = open("image.jpg", "wb") # opens the image.jpg file for writing in binary (data of the image will be added to the repl)
f.write(picture.content) #writes the image to the file  
f.close() #closes the file

print(image)
```
👉 Y aquí está todo el código:

```python
import requests, json #imports the json library

result = requests.get("https://randomuser.me/api/")
user = result.json() #a dictionary containing the user's data
# print(json.dumps(user, indent=2)) #outputs the json to the console with an indent to make it more readable.

name = f"""{user["results"][0]["name"]["first"]} {user["results"][0]["name"]["last"]}""" # Get the first and last names from the results dictionary and assign to a variable

image = f"""{user["results"][0]["picture"]["medium"]}""" # Get the user's profile picture and assign to a variable, changing 'medium' to 'large' will make the image less pixelated
picture = requests.get(image) #downloads the image
f = open("image.jpg", "wb") # opens the image.jpg file for writing in binary (data of the image is added to the repl)
f.write(picture.content) #writes the image to the file  
f.close() #closes the file

print(image) # output the variable

```

## Loops Loops Loops
👉 Podríamos usar un bucle para conseguir lo mismo, pero haciendo nuestro código un poco más ordenado y legible. Sólo obtenemos un usuario de vuelta de este sitio web, pero este código se ocuparía de múltiples usuarios también.

He vuelto a la salida sólo el nombre para simplificar el ejemplo. Aquí está el código:
``python
import requests, json

result = requests.get("https://randomuser.me/api/")
user = result.json()
# print(json.dumps(user, indent=2)) 

for person in user['results']: #loops through each person in the results dictionary
  name = f"""{person["name"]["first"]} {person["name"]["last"]}""" #creates a string with the name of the person

  print(name)#prints the name of the person
```

## ¡Pruébalo!

# 👉 Desafío del día 90

El reto de hoy consiste en utilizar el código que acabas de ver para extraer los datos de 10 usuarios utilizando de nuevo *randomuser.me*.

Tu programa debería:

1. Guardar la versión de calidad media de la foto de perfil como un archivo local llamado *{firstName} {lastName}.jpg*.
2. Cada imagen debe guardarse en un archivo diferente.
    
<detalles> <sumario> 💡 Consejos </sumario>
  
- Utiliza un bucle for para enviar 10 peticiones, por ejemplo: ` for persona en usuario[«resultados»]:`.

</detalles>