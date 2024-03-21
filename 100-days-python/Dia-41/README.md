# Diccionarios con bucles

Los bucles y las listas forman una pareja perfecta. Los diccionarios y los bucles son un poco más complicados.  Esto se debe a que cada elemento del diccionario se compone de dos partes - el nombre de la clave y el valor real de esa clave.



## ¡He Perdido Mis Llaves!
Creemos un diccionario en bucle.

👉 Usar un bucle `for`, como haríamos con una lista, mostrará los valores, _pero no las claves_.  No es lo ideal. 

```
miDiccionario = {"nombre" : "Ian", "salud": 219, "fuerza": 199, "equipado": "Hacha"}

para i en miDiccionario
  print(miDiccionario[i])

```
##
👉 Este bucle utiliza el método `.values()`, que se puede ejecutar sobre un tipo de datos. Seguimos obteniendo sólo el valor, y no la clave.

```
miDiccionario = {"nombre" : "Ian", "salud": 219, "fuerza": 199, "equipado": "Hacha"}

para valor en miDiccionario.values():
  print(valor)

```

## Tengo La Llave...Tengo El Secreto

¡Hay una forma mejor! 

Aquí tienes un bucle que mostrará la clave **y** el valor.  

👉 La función `.items()` devuelve el nombre de la clave y el valor. Tenga en cuenta que he suministrado el bucle con dos argumentos: `nombre` y `valor`).

Este ejemplo sólo mostrará los nombres y valores usando un fString.

```
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")
```

## Un poco confuso

Vayamos un paso más allá y utilicemos algunas sentencias `if` dentro del bucle.

👉 Este ejemplo hace un comentario sobre la clave de fuerza.

```
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    print("Whoa, SO STRONG!")
```
👉Este ejemplo usa sentencias `if` anidadas** para reaccionar al nombre de la clave **y** al valor almacenado en ella.

```
myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    if value > 100:
      print("Whoa, SO STRONG")
    else:
      print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")
```

### ¡Pruébalo y aprovecha el poder de la iteración con tu diccionario!

# Errores comunes

*Primero, borra cualquier otro código de tu fichero `main.py`. Copia cada fragmento de código en `main.py` haciendo clic en el icono de copia en la parte superior derecha de cada cuadro de código. A continuación, pulsa `run` y comprueba qué errores se producen. Corrige los errores y pulsa "run" de nuevo hasta que estés libre de errores. Haz clic en "Respuesta" para comparar tu código con el correcto.

## ¡Haz que desaparezcan los paréntesis!

👉 ¿Cuál es el problema aquí?

```
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name in myDictionary.items():
  print(f"{name}")
```

<detalles> <sumario> 👀 Respuesta </sumario>

Sólo le hemos dado al bucle una variable en lugar de dos.
```python
miDiccionario = {"nombre" : "Ian", "salud": 219, "fuerza": 199, "equipado": "Hacha"}

para nombre, valor en miDiccionario.items():
  print(f"{nombre} {valor}")
```

</detalles>

# 👉 Desafío del día 41

1. Crea un diccionario que almacene la siguiente información sobre una página web: nombre, URL, descripción y una valoración con estrellas (sobre 5).
2. Utiliza un bucle para dar salida a los nombres de las claves, pedir al usuario que escriba los datos y almacenar la entrada en el diccionario.
3. Por último, muestra el diccionario completo (claves y valores).


🥳 Puntos extra por obtener todas las entradas con un solo comando `input` y la función `split`.

Ejemplo:

```
🌟Calificación del sitio web🌟

Introduce el nombre del sitio web: Replit

Introduzca la URL: replit.com

Introduzca su una descripción: Un IDE en línea impresionante.

Introduzca la calificación a de 5 estrellas: *****

nombre:Replit, URL:replit.com, descripción:Un IDE en línea impresionante, puntuación:***** 
```

<detalles> <sumario> 💡 Consejos </sumario>

- Al crear su diccionario, tendrá que utilizar `ejemplo = { "MyValue": none}` para mostrar un nombre de clave y ningún valor.
- Utilice un bucle para `imprimir` todo el diccionario.
- Asegúrate de incluir ambas variables (nombre y valor) en tu bucle y en tu sentencia `print`.

</detalles>

La solucion la encontramos en [main.py](./main.py)