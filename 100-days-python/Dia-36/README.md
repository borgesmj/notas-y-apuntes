# Manipulacion de la cadana de caracteres
Hagamos algo de manipulacion para hacer que las declaraciones `if` mas faciles.

¿Este codigo te parece familiar?
```
name = input("What's your name? ")
if name == "David" or name == "david":
  print("Hello Baldy!")
else: 
  print("What a beautiful head of hair!")
```

Ahora, si el usuario escribe "DAVID" o "david", la declaracion `if` resultará correcta. Sin embargo, "DaVId" no regresará la respuesta correcta

Para la computadora, " david", "dAvId", y "david" son completamente distintos.

Para simplificar lo que el usuario coloca en el input, podemos añadir estas funciones al final de la variable

* `stringName.lower()`: todas las letras a minusculas.
* `stringName.upper()`: todas las letras a mayusculas
* `stringName.title()`: Convierte en mayusculas la primera letra de todas las palabras
* `stringName.capitalize()`: convierte en mayuscula solamente la primera letra de la primera palabra

## ¿Y si colocaramos un espacio en blanco al comienzo?
Añadiendo un `.strip()` eliminamos el espacio en blanco en ambos lados de la palabra

```
name = input("What's your name? ")
if name.lower().strip() == "david": 
  print("Hello Baldy!")
else: 
  print("What a beautiful head of hair!")
```

## Sin duplicados
Este es un ejemplo de programa que crea una lista, con una subrutina simple. En el bucle `While True`el usuario esta añadiendo algo a la lista.

```
myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  addItem = input("Item > ")
  if addItem not in myList:
    myList.append(addItem) 
  printList()
```

Aqui hay una manera mas facil de asegurarnos que no haya duplicados. Usando varias manipulaciones de string dentro del loop

```
myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  addItem = input("Item > ").capitalize().strip() #Lo colocamos en mayusculas y eliminamos los espacios en blanco
  if addItem not in myList:
    myList.append(addItem)
  printList()
```


## Errores comunes
### El orden importa
¿que pasa si añadimos ` phone` a esta lista?

```
myList = []

def printList():
 print()
 for i in myList:
   print(i)
 print()

while True:
 addItem = input("Item > ").capitalize().strip()
 if addItem not in myList:
   myList.append(addItem)
 printList()
```

la funcion `.capitalize()` va a colocar en mayuscula el primer caracter, que en este caso es un espacio en blanco, y luego lo eliminará, por eso no se ven cambios si lo agregamos a la lista, para solucionar esto, cambiemos el orden:

```
while True:
addItem = input("Item > ").strip().capitalize()
if addItem not in myList:
  myList.append(addItem)
printList()

```

## Reto del dia
* Elabore una lista con los nombres de las personas. Pide el nombre y los apellidos por separado.
* Elimine los espacios sobrantes.
* Guarde los nombres en mayúsculas.
* Crea una nueva cadena utilizando una fString que combine la versión ordenada del nombre y la versión ordenada del apellido.
* Añada esas nuevas versiones a una lista.
* No permita duplicados.
* Cada vez que añada un nuevo nombre, imprima la lista completa.

La solución esta en [main.py](./main.py)