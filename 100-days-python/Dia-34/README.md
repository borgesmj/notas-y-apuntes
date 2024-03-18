# Funciones Pretty Print

Construyamos una subrutina pretty `print()`. Hasta ahora, las subrutias que hemos hecho, son un poco... aburridas.

Cuando tenemos una lista de informacion, ser capaz de imprimir esa data en maneras bonitas es una capacidad que debemos tener. Asi que "pretty printing" es algo real.

Está este ejemplo de programa que llamamos "Spammer Inc.", para spammear emails (obviamente no es algo que haremos realmente). Si el usuario presiona 1, puede añadir un email, y presionando 2 le permite borrar ese email (hasta ahora eso nos puede parecer familiar)

```
import os, time
listOfEmail = []

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  time.sleep(1)
  os.system("clear")
```

Lo que aun no hemos hecho es `print()`. ÑAdamos una funciob pretty `print()`

```
import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") # start by clearing the screen
  print("listofEmail") # print the title of my program
  print() # print a blank line
  for email in listOfEmail: # use for loop to access list
    print(email)
  time.sleep(1)

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
    prettyPrint()  
  time.sleep(1)
  os.system("clear")
```

## Creando una lista numerada
Tambien podemos enumerar nuestra lista. Hagamos que esto suceda haciendo unos cambios dentro de nuestra subrutina. Este codigo solo muestra la subrutina, asi qeu nos podemos enfocar en los cambios aqui:

```
def prettyPrint():
os.system("clear") 
print("listofEmail") 
print()
counter = 1 # add a counter
for email in listOfEmail: 
  print(f"{counter}: {email}") # make this an f-string
  counter += 1 # adds a number with each new email
time.sleep(1)
```

```
import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  counter = 1 
  for email in listOfEmail: 
    print(f"{counter}: {email}") 
    counter += 1 
  time.sleep(1)

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3": # we added this elif
    prettyPrint() # called our subroutine here
  time.sleep(1)
  os.system("clear")
```

## Usando el index
También podemos utilizar bucles de una manera ligeramente diferente para acceder a los elementos de una lista (o matriz). De la forma en que tenemos nuestro código escrito ahora, nuestra lista crea una variable llamada email, la establece igual al primer valor (con nuestro contador establecemos 1 como primer valor), y luego cuenta a medida que avanzamos. (2, 3, 4, etc.)

Sin embargo, también podemos configurar el bucle for para utilizar el índice. Lo que debería pasar es que el índice empezará en 0, recorrerá todo el código del bucle en 0, volverá al principio del bucle, añadirá 1, y luego hará el bucle una y otra vez hasta que termine la lista.....

Vamos a modificar un poco el bucle for de nuestra subrutina para conseguir esto:

```
import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)): # len counts how many items in a list
    print(f"{index}: {listOfEmail[index]}") 
  time.sleep(1)


while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  time.sleep(1)
  os.system("clear")
```

## Errores comunes
¿Puedes ver que hay de error en este codigo?

```
import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in len(listOfEmail): 
    print(f"{index}: {listOfEmail[Index]}") 
    counter += 1 
  time.sleep(1)


while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  time.sleep(1)
  os.system("clear")
```

## Reto del dia
Ampliemos este programa y construyamos la opción 4: "GEt SPAMMING".

Imprime las 10 primeras direcciones de correo electrónico con un correo personalizado enviado a cada una de esas personas.
Imprima un email a la vez, haga una pausa y luego limpie la pantalla antes de imprimir el siguiente email.
Ejemplo:

```
Dear john@test.com
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
Ian Spammington III
```


La solucion la encontramos en [main.py](./main.py)s