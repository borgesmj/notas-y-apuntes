# Cambio de tipo

Las declaraciones if soportan mas que `==`. Soportan simbolos de desigualdad tambien. ¿Recuerdas esas `>`, `<` y `=` que usabamos en la escuala hace mucho tiempo? BUeno, esán de vuelta, pero esta vez un poco diferentes.

## Simbolos de desigualdad
```
# equal
5 == 5

# not equal
3 != 5

# greater than
5 > 3

# greater than or equal to
5 >= 3

# less than
3 < 5

# less than or equal to
3 <= 5
```

Esto es porque los `input()` trabajan detras de bastidores asumiendo que todo lo que tipeamos es un string, y se guardan en variables junto con `" "`.

CAmbio de tipo es donde le decimos explicitamente al computador que estamos tipeando numeros y no letras

El siguiente codigo asigna gaador al usuario si tiene 100.000 o mas puntos, de otra manera que intente de nuevo.

Copialo y pegalo y ponlo a correr, luego coloca la  cantidad de puntos y mira que pasa

```
myScore = input("Your score: ")
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
```

El programa se *crashea* porque le estamos introduciendo texto, en lugar de un numero al que se le pueda hacer una comparacion

Esto se soluciona añadiendo un *int* (numero entero) o un *float* (numero con decimales) para convertirlos.

Intentemos añadiendo un `int` delante del input y encerrando todo el input con `()`

```
myScore = int(input("Your score: "))
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
```

¿Ahora si funcionó?
La manera que el computador va a leer el codigo es comenzando que todo lo que está dentro de las comillas primero, el computador piensa que es un texto por `" "`, pero cuando le añadimos un `int` le estamos diciendo que no es un texto, es un numero entero.

¿Pero que tal un `float`?

Se hace exactamente lo mismo pero con un `float()` al principio, para numeros decimales.

```
myPi = float(input("¿Cuanto es el valor de PI? "))
if myPi == 3.1416:
  print('Exacto')
else:
  print('Intenta de nuevo 😭')
```

## Errores Comunes
### Invalid Syntax
¿Cual es el error?
```
myPi = float(input("What is Pi to 3dp? ")
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")
```

*Respuesta:* Olvidamos el segundo parentesis de cierre `)` al final del input, recuerda qeu cada linea que tenga un simbolo de abertura necesita un simbolo de cierre

### Reto extra
¿Cual es el error?
```
myPi = float input("What is Pi to 3dp?")
if myPi == 3.142 :
  print("Exactly!)
else:
  print("Try again 😭")
```

*Respuesta:* no hay parentesis de abertra ni de cierre para el float, debemos encerrar entre parentesis todo lo que queramos cambiar de tipo. Tampoco hay comillas de cierre en `print("Exactly!)`

## Arregla mi codigo
Arregla este código

```
score = input("What was your score on the test?"))
if score >= 80
  print("Not too shabby")
elif score > "70":
  print("Acceptable.")
else:
print("Dude, you need to study more!")
```

Aqui tienen el codigo solucionado:

```
score = int(input("What was your score on the test? "))
if score >= 80:
  print("Not too shabby")
elif score > 70:
  print("Acceptable.")
else:
  print("Dude, you need to study more!")
```

## Reto del dia
Generador de generaciones
¿A que generacion pertenecemos?
Utiliza esta tabla como guia
| Nombre de la generacion | Inicio Año de nacimiento | Fin año de nacimiento |
|-------------------------|--------------------------|-----------------------|
| Taadicionalistas        | 1925                     | 1946                  |
| Baby Boomers            | 1947                     | 1964                  |
| Generacion X            | 1965                     | 1981                  |
| Millenials              | 1982                     | 1995                  |
| Generacion Z            | 1996                     | 2015                  |

1. Pidele al usuario que introduzca su año de nacimiento
2. Utiliza su respuesta para decirle a que generacion pertenece
3. Utiliza emojis para crear respuestas mas divertidas

Mi solucion la encuentran en [main.py](./main.py)