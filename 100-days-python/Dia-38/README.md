# Strings y bucles
Bueno, ahora que sabemos que los string son, basicamente, listas, podemos comenzar a usar el poder de los bucles en ellos

## Usando el bucle `for`
Este bucle for crea una variable llamada `letter` que se usa para guardar cada caracter en el string mientras el bucle avanza dentro de él, comenzando en el primer caracter

```
myString = "Day 38"
for letter in myString:
  print(letter)

# This code outputs:
#D
#a
#y

#3
#8
# this is a comment in the code, the computer will ignore it
```
e
La declaracion `print()` usa la variable _letter_ y la va aimprimir un caracter a la vez

Esto quiere decir que podemos hacer ciertas cosas dentro del bucle

## Declaracion `if` dentro del bucle
Este codigo examina la version en minuscula de cada caracter. Si es una 'a', la compuadora va a cambiar el color a amarillo antes de imprimirlo.
Fuera del loop, la ultima linea va a configurar el color de la fuente de vuelta a por defecto, para el siguiente caracter en el bucle.

```
myString = "Day 38"
for letter in myString:
  if letter.lower() == "a":
    print('\033[33m', end='') #yellow
  print(letter)
  print('\033[0m', end='') #back to default

# This code outputs (with a yellow 'a'):
#D
#a
#y

#3
#8
```
## Utilizando una lista para especificar una busqueda de items
```
vowels = ["a","e","i","o","u"]

myString = "Will my vowels now be yellow?"
for letter in myString:

  if letter.lower() in vowels:
    print('\033[33m', end='') #yellow

  print(letter, end="")
  print('\033[0m', end='') #back to default
```

## Reto del dia: Codifica el arco iris

1. Pide al usuario que introduzca una frase cualquiera (cadena).
2. Ahora la convertiremos en arco iris (no, yo tampoco).
3. En cuanto la cadena contenga una "r", todas las letras a partir de ese punto serán rojas.
4. Cuando el ordenador encuentre una "b", una "g", una "p" o una "y", la salida será azul para la "b", verde para la "g"... ya te haces una idea.
5. Haz un bucle a través de la cadena y sácala (para que el color continúe a través del bucle).
6. La salida debe cambiar de color cada vez que se encuentra con un nuevo r,g,b,p o y.

🥳 Puntos extra por restablecer el color de salida por defecto cada vez que hay un espacio.

LA solucion la encontramos en [main.py](./main.py)