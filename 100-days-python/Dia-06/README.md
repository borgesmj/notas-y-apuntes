# ¿QUE ES **elif**?

El comando *elif* (que viene de *else if*), nos permite preguntar 2, 3, 4, 0 150 preguntas al usuario usando el mismo input. Este comando debe estar en un luigar en especifico. Podemos tener muchos *elif* como nos sea necesario, pero deben ir entre el *if* y el *else* y debe tener la misma indectacion. LA declaracion *print()* en el comando *elif* debe alinearse con los otros *print()* de las demas declaraciones.

¿Donde iria un *elif* en el c´digo de abajo?

```
print('LOGIN SEGURO')
username = input('username > ')
if username == 'mark':
    print('Bienvenido Mark')
else:
    print('vete!')
```

El comando *elif* iria entre el *if* y el *else*, quedando de esta manera


```
print('LOGIN SEGURO')
username = input('username > ')
if username == 'mark':
    print('Bienvenido Mark')
elif username == 'suzanne':
    print('Bienvenida Suzanne')
else:
    print('vete!')
```

## Añadiendo contraseñas
Añadamos un poco mas de input

Ahora podemos añadirle otro input para el password para que nuestro login sea mas seguro

```
print('LOGIN SEGURO')
username = input('username > ')
password = input('password > ')
print()
if username == 'mark' and password == "password":
    print('Bienvenido Mark')
elif username == 'suzanne':
    print('Bienvenida Suzanne')
else:
    print('vete!')
```

la contraseña de Suzane es 'Su74nne', vamos a añadirla

```
print('LOGIN SEGURO')
username = input('username > ')
password = input('password > ')
print()
if username == 'mark' and password == "password":
    print('Bienvenido Mark')
elif username == 'suzanne' and password == "Su74nne":
    print('Bienvenida Suzanne')
else:
    print('vete!')
```

## Errores comunes

### Syntax Error
¿Que hay de malo en el siguiente código?

```
print("SECURE LOGIN")
username = input("Username > ")

if username == "mark":
  print("Welcome Mark!")
else:
  print("Go away!")
elif username == "suzanne":
  print("Hey there Suzanne!")
```
> **Respuesta:** el *elif* esta fuera de los limites del *if* y *else*

## Arregla este código

```
season = input(what is your favorite season?)
if season = "spring"
  print("Ah! The birds are chirping and flowers blooming.")
  elif season == summer:
  print("Catch some sun and cool off with a lemonade.")
elif season == autumn
print("The leaves are changing and the air is crisp. Enjoy!)
      elif season = winter:
      print("Stay warm by the fire and watch the snow fall.")
else: 
print("I don't know that season. Please try again.")
```

Solución

```
season = input("what is your favorite season? ")
if season == "spring":
  print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
  print("Catch some sun and cool off with a lemonade.")
elif season == "autumn":
  print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
  print("Stay warm by the fire and watch the snow fall.")
else: 
  print("I don't know that season. Please try again.")
```

## Reto del dia 6
Hagamos nuestro propio login
1. Creemos un programa donde alguien pueda hacer login con su username y contraseña correctamente y obtenga un saludo personal
2. Escribamos un saludo personalizado para tres diferentes personas
3. NO olvidemos la declaracion else para quienes no deberian estar.

La solucion a este reto la encontramos en [main.py](./main.py)