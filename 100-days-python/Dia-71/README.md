# Se llama Hashing

Uno de los grandes problemas de almacenar nombres de usuario y contraseñas en una base de datos es *¿qué pasa si nos piratean*?

Si esas contraseñas se almacenan como texto, la seguridad de nuestros usuarios se ve comprometida. Probablemente en varios sitios porque **ignoraron nuestro consejo y usaron la misma contraseña para todo!!!!!**.


## Hashing

En realidad, las organizaciones *no almacenan su contraseña real*. Almacenan un hash de tu contraseña. Un hash se produce convirtiendo tu contraseña en una secuencia de números y pasándola por un algoritmo hash (un proceso matemático muy difícil de descifrar). Los datos escupidos por este algoritmo son los que se almacenan en lugar de tu contraseña real.

Así que vamos a hacerlo. Estoy usando la función `hash` para crear un hash numérico de la contraseña. 

```python
password = "baldy1"
password = hash(password)
print(password)

# This will output a really long number
```
Juega con diferentes cadenas en la línea 1 y observa como el número hash cambia completamente.

👉 Ahora vamos a almacenar esa versión hash en nuestra base de datos en lugar de la contraseña real.

```python
from replit import db

userName = "david"
password = "baldy1"
password = hash(password)
db[userName] = password # Stores the hashed password in the database under the username key 'david'

print(password)
```

## Imprimiendo el Hash
👉 Ahora puedo imprimir el valor de la base de datos usando print. Fíjate como muestra el hash. Eso será inútil para un hacker. Ellos no pueden fácilmente revertir la ingeniería de la contraseña desde el hash.

```python
from replit import db

print(db["david"])

```

Para acceder a un usuario, obtenemos su contraseña, la introducimos, le aplicamos el hash, y la comparamos con el hash almacenado en la base de datos porque **una cadena siempre producirá el mismo valor hash**.

Construyamos el sistema de login que compara el hash almacenado con el hash de la entrada.

```python
from replit import db

ask = input("Contraseña >") # Obtener la entrada
ask = hash(ask) # Hash de la entrada

if ask == db["david"]: #compara el hash de la entrada con el hash almacenado.
 print("Inicio de sesión correcto")

```


### ¡Pruébalo!

# ¡Oooh, Salty!

Los hash son geniales, pero los hackers han creado su propia base de datos con los hash de casi todas las palabras y contraseñas habituales.

Así que lo más probable es que, si utilizas una contraseña común o una palabra cotidiana, haya un hash de ella en algún lugar de Internet esperando una búsqueda inversa.

Para evitarlo, podemos generar un valor aleatorio y añadirlo al final de la contraseña antes de realizar el hash. Este valor aleatorio se llama **sal**.

👉 Pongámosle sal al hash de nuestra contraseña de antes.

``python
from replit import db

contraseña = "Calvo1"
salt = 10221

nuevaContraseña = f"{contraseña}{sal}" # añadir la sal
nuevaContraseña = hash(nuevaContraseña) # hash del lote

print(nuevaContraseña)
```
## Segundo Usuario
👉 Si tenemos un segundo usuario con la misma contraseña, la sal generada de forma única (me las acabo de inventar en estos ejemplos) producirá un hash *completamente diferente*. 
``python
from replit import db

contraseña = "Calvo1"
sal = 10221
nuevaContraseña = f"{contraseña}{sal}"
nuevaContraseña = hash(nuevaContraseña)
print(nuevaContraseña)

contraseña = "Calvo1"
sal = 39820
nuevaContraseña = f"{contraseña}{sal}"
nuevaContraseña = hash(nuevaContraseña)
print(nuevaContraseña)
```

👉 Para hacer frente a esto, necesitaríamos nuestra base de datos para almacenar la contraseña hash **y** la sal. Hacemos esto usando un diccionario.

``python
from replit import db

contraseña = "Calvo1"
sal = 10221
nuevaContraseña = f"{contraseña}{sal}"
nuevaContraseña = hash(nuevaContraseña)
print(nuevaContraseña)

db["david"] = {"contraseña":nuevaContraseña, "sal": sal}

```

👉 Ahora vamos a actualizar el sistema de login para que saque la sal de la base de datos, la añada a la contraseña introducida y luego haga un hash del lote. Después de eso, podemos compararlo con el hash almacenado de la contraseña y la sal del ejemplo anterior.

``python
from replit import db

ans = input("Contraseña >") # Obtener la entrada
salt = db["david"]["salt"] # Obtener la sal de la base de datos.
nuevaContraseña = f"{ans}{sal}"
nuevaContraseña = hash(nuevaContraseña) # Hash de la cadena concatenada

if nuevaContraseña == db["david"]["contraseña"]: #compara el hash de nuevaContraseña con el hash almacenado.
 print("Inicio de sesión correcto")

```

### ¡Pruébalo!

# ¡Oooh, Salty!

Los hash son geniales, pero los hackers han creado su propia base de datos con los hash de casi todas las palabras y contraseñas habituales.

Así que lo más probable es que, si utilizas una contraseña común o una palabra cotidiana, haya un hash de ella en algún lugar de Internet esperando una búsqueda inversa.

Para evitarlo, podemos generar un valor aleatorio y añadirlo al final de la contraseña antes de realizar el hash. Este valor aleatorio se llama **sal**.

👉 Pongámosle sal al hash de nuestra contraseña de antes.

```python
from replit import db

password = "Baldy1"
salt = 10221

newPassword = f"{password}{salt}" # append the salt
newPassword = hash(newPassword) # hash the lot

print(newPassword)
```
## Segundo Usuario
👉 Si tenemos un segundo usuario con la misma contraseña, la sal generada de forma única (me las acabo de inventar en estos ejemplos) producirá un hash *completamente diferente*. 
```python
from replit import db

password = "Baldy1"
salt = 10221
newPassword = f"{password}{salt}"
newPassword = hash(newPassword)
print(newPassword)

password = "Baldy1"
salt = 39820
newPassword = f"{password}{salt}"
newPassword = hash(newPassword)
print(newPassword)
```

👉 Para hacer frente a esto, necesitaríamos nuestra base de datos para almacenar la contraseña hash **y** la sal. Hacemos esto usando un diccionario.

```python
from replit import db

password = "Baldy1"
salt = 10221
newPassword = f"{password}{salt}"
newPassword = hash(newPassword)
print(newPassword)

db["david"] = {"password":newPassword, "salt": salt}
```

👉 Ahora vamos a actualizar el sistema de login para que saque la sal de la base de datos, la añada a la contraseña introducida y luego haga un hash del lote. Después de eso, podemos compararlo con el hash almacenado de la contraseña y la sal del ejemplo anterior.

```python
from replit import db

password = "Baldy1"
salt = 10221
newPassword = f"{password}{salt}"
newPassword = hash(newPassword)
print(newPassword)

db["david"] = {"password":newPassword, "salt": salt}

```

### ¡Pruébalo!

# Errores comunes

*Primero, borra cualquier otro código de tu fichero `main.py`. Copia cada fragmento de código en `main.py` haciendo clic en el icono de copia en la parte superior derecha de cada cuadro de código. A continuación, pulsa `run` y comprueba qué errores se producen. Corrige los errores y pulsa "run" de nuevo hasta que estés libre de errores. Haga clic en "Respuesta" para comparar su código con el código correcto.

## NO estoy entrando

👉 ¿Cuál es el problema?


```python
from replit import db

ans = input("Password >") 
salt = db["david"]["salt"]
newPassword = f"{ans}{salt}"
newPassword = hash(newPassword) 

if ans == db["david"]["password"]: 
  print("Login successful")
```

<detalles> <sumario> 👀 Respuesta </sumario>

Estábamos comprobando la entrada *pre hash* en la variable 'ans' en lugar de los datos *post hash* en la variable 'newPassword'.

```python
from replit import db

ans = input("Password >") 
salt = db["david"]["salt"] 
newPassword = f"{ans}{salt}"
newPassword = hash(newPassword) 

if newPassword == db["david"]["password"]: #compare hash of newPassword to stored hash.
  print("Login successful")
```

</detalles>

## Retener La Sal

👉 ¿Cuál es el problema aquí?
```python
from replit import db

ans = input("Password >") 
salt = db["david"]["salt"] 
newPassword = f"{salt}{ans}"
newPassword = hash(newPassword) 

if newPassword == db["david"]["password"]: 
  print("Login successful")
```

<detalles> <sumario> 👀 Respuesta </sumario>

Hemos concatenado la sal al principio de la contraseña en el fString. Debería ir al final.

```python
from replit import db

ans = input("Password >") 
salt = db["david"]["salt"] 
newPassword = f"{ans}{salt}" # the salt should go on the end of the password
newPassword = hash(newPassword) 

if newPassword == db["david"]["password"]: 
  print("Login successful")
```


</detalles>

# 👉 Desafío del día 71

El reto de hoy consiste en construir un sencillo sistema de inicio de sesión.

Su programa debe:

1. Mostrar un menú con la posibilidad de añadir un usuario o iniciar sesión.
2. 'Añadir' usuario debería:
    * Pedir un nombre de usuario y una contraseña.
    * Crear una nueva contraseña y una sal de 4 dígitos generada aleatoriamente.
    * Añada la sal a la contraseña y haga un hash.
    * Almacenar el hash y la sal en una repl db con el nombre de usuario como clave.
3. 'Login' debería:
    * Obtener el nombre de usuario y la contraseña.
    * Mostrar un mensaje de éxito si los datos son correctos.
4. Este sistema debería funcionar con múltiples usuarios.


Ejemplo:

```
🌟Login System🌟

1: Add User, 2: Login >  1

Username: > Kenny
Password: > L0gg1ns

Details stored.

1: Add User, 2: Login >  2

Username: > Kenny
Password: > L0gg1ns

Login successful
```

<detalles> <sumario> 💡 Sugerencias </sumario>

- Intenta implementar las dos opciones de menú como subrutinas. Podrás portarlas a otros programas más fácilmente. 

</detalles>