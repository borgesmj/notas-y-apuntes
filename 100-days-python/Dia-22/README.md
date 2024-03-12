# Dia 22: Librerias

Librerias son colecciones de codigo que otras personas ya han escrito.
Video juegos usualmente utilizan muchas librerias (por ejemplo: [game engines](https://en.wikipedia.org/wiki/List_of_game_engines)) para crear ese reflejo epico en el agua, graficos #d etc.

VAmos a comenzar un poco mas pequeños, solo generando numeros aleatorios (despues de todo, [numeros aleatorios son la base de la mayoria de juegos](https://www.gamedeveloper.com/programming/how-classic-games-make-smart-use-of-random-number-generation))

## Libreria `Random`
Podemos utilizar una libreria escribiendo `import`y luego el nombre de la libreria.

_Esto debe ser siempre en las primeras lineas de codigo_

Importemos la libreria que genera numeros aleatorios:

```
import random
```

## ¿Como funciona `random`?
En el siguiente codigo, hemos creado una variable, "myNumber". Lo estamos igualando a un numero aleatorio que se me ha dado por medio de la libreria `randint` (random integer). Añadimos el numero mas bajo en el rango (1) y el numero mas alto (100) y la computadora genera el numero aleatorio.

```
import random
myNumber = random.randint(1,100)
print(myNumber)
```

## ¿Que hago con las librerias?
Antes, teníamos que codificar el valor que buscaban los usuarios (recuerde el juego de adivinar si era mayor o menor...).

Con random, podemos generar el numero que ni si quiera nosotros mismos sabremos.

## Errores comunes

### Name error
```
import random

myNumber = randint(1, 100)
print(myNumber)
```

Este error es por la manera que trabaja la libreria. Los nombres de las funciones y variables en las librerias pueden ser similares a los nombres que elegí para mis funciones y variables. La forma de acceder a las funciones y variables de otras librerias es poner random. delante del nombre de la biblioteca.

```
import random

myNumber = random.randint(1, 100)
print(myNumber)
```

Ahora la computadora sabe que debe ir a la libreria `random` y encontrar `randint` ydarme un numero entre 1 y 100

### Error con numeros aleatorioa y bucles
Para este codigo, queremos 10 numeros aleatorios entre 1 y 100. ¿Por qué está imprimiendo el mismo numero en lugar de 10 numeros aleatorios distintos?

```
import random

myNumber = random.randint(1, 100)
for i in range(10):
  print(myNumber)
```

Esto se debe a que el numero aleatorio fue llamado una unica vez fuera del bucle, la solucion es meterlo dentro del bucle for

```
import random

for i in range(10):
  myNumber = random.randint(1, 100)  
  print(myNumber)
```

Reto: Copia y pega el codigo del [dia 18](../Dia-18/main.py) vamos a hacer un cambio en este proyecto; haz que el numero a adivinar sea totalmente aleatorio entre 1-1.000.000 (ahora el usuario no puede hacer trampa)

La solucion la encontramos en [main.py](./main.py)