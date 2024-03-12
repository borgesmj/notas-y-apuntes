# Estructura de control
Este dia trabajaremos con las declaraciones *if*, *match* (que en otros lenguajes es "switch"), foreach, while

Tambien trabajaremos con booleanos (True, False)
Operadores relacionales (==, !=, >, >=, <, <=)
Operadores logicos (and, orn not )

Ejemplos de operadores relacionales

```
number1 = 10
number2 = 20

result = number1 == number2
print(result)
# nos regresa False

```
Operadores relacionales siempre nos regresará un booleano.

## Operadores logicos

+ and: para que el resultado de dos o mas comparaciones, todas deben ser True, sin importar si colocamos 2 o 100, absolutamente todas se deben cumplir.
+ or: basta con que una sola de todas las comparaciones sean True, la operacion nos regresará Trua
+ not negar la operacion, invierte los resultados de la operacion.
```
number1 = 10
number2 = 20

result = number1 == number2 and 10 == 9 
print(result)# False
result2 = number1 == number2 or 10 == 10 
print(result2) # True
result3 = number1 != number2 and 10 == 10 # el resultado es True
print(not result3) # pero con el operador logico not, nos regresa False
```

## Declaraciones

+ if: un bloque de codigo se ejecutará cuando un condicion se cumple
+ else: esta opcion se ejecuta cuando la condicion no se cumple.

Por ejemplo, si le pedimos la edad a un usuario
```
age = int (input('Ingresa tu edad > ')) # el int es para verificar que solo ingrese numeros enteros
if age >= 18:
  print('Tienes la edad para votar')
else:
  print('Los entimos, no puedes votar')
```

Pero ¿que pasa con este codigo? Si un usuario coloca 1001, para el sistema seguirá siendo válido popr ser *>=18*, asi que usaremos condiciones anidadas
```
age = int (input('Ingresa tu edad > ')) # el int es para verificar que solo ingrese numeros enteros
if age < 110:
  if age >= 18:
    print('Tienes la edad para votar')
  else:
    print('Los entimos, no puedes votar')
else:
  print('Ingresa una edad valida')
```
El código primero evalua que sea una edad válida, menor a 110 y luego evalua si puede o no votar
Y si le colocamos para que valide que el numero sea positivo e todo momento

```
age = int (input('Ingresa tu edad > ')) # el int es para verificar que solo ingrese numeros enteros
if age > 0 and age < 110:
  if age >= 18:
    print('Tienes la edad para votar')
  else:
    print('Los entimos, no puedes votar')
else:
  print('Ingresa una edad válida')
```
## Condiciones anidadas
Supongamos que tenemos un semaforo:

```
color = 'yellow'

if color == 'green':
  print('puede continuar')
else:
  if color == 'yellow':
    print('precaucion')
  else:
    if color == 'red':
      print('pare')
    else:
      print('color no valido')
```

Este codigo no es mantenible, asi qeu podemos apoyarnos de un *elif* (else if)
```
color = 'yellow'

if color == 'green':
  print('puede continuar')
elif color == 'yellow':
  print('precaucion')
elif color == 'red':
  print('Detengase')
else:
  print('color no valido')
```

## Switch
Podemos mejorar aun mas el codigo usando el switch
```
color = 'red'

match color:
  case 'red':
    print('pare!')
  case 'yellow':
    print('alto parcial')
  case 'green':
    print('avance')
  case _: # case con un guion bajo, python lo interpreta como el else final
    print('ese color no existe')
```

## foreach y while
+ foreach => se utiliza cuantas iteraciones se necesitan
+ while => cuando NO sepamos cuantas iteraciones se necesitan (condiciones)

### foreach
En python se encuentran diferentes objetos con los cuales iterar, estos objetos son llamados *colecciones*, hasta ahora solo hemos trabajado con los string, que son una coleccion de caracteres

```
title = 'Estructura de control'

for caracter in title:
  print(caracter)
```
Este codigo evaluara y hara el bloque de codigo para cada caracter del string

Iterar en rango establecido
```
for number in range(1,101): # un rango del 1 al 100, el 101 no lo tomará en cuenta
  print (number)
```
Pero claro que no solo podemos imprimir el numero solamente, podemos colocar condicionales
```
for number in range(1,101):

  if number % 2 == 0: # si el número es divisible entre 2, es decir, si es par
    print(number)
```

### while
La estructura while seguira iterando mientras una condicion se cumpla

```
while <condicion>:
    bloque de codigo
    contador
```

ejemplo:
```
number = 0

while number < 10:
  print(number)
  number += 1
else:
  print("TLa condicion no se cumple")
```

Un ultimo ejemplo antes de comenzar con el reto
```
attends = 0
random = 5
number = 0
max_attends = 5

while number != random and attends < max_attends:

  number = int(input('Ingresa un numero: '))
  attends += 1

else:

  if number == random:
    print('Ganaste')
  else:
    print('Perdiste')
```
Este codigo "genera un numero aleatorio" y el usuario deberá adivinarlo en un maximo de 5 intentos, mientras se cumplan las condiciones del while `number != random and attends < max_attends` seguirá solicitando un número, cuando ya cuando una de las dos se rompa, pasará a declarara ganador o perdedor

## Reto del dia:

Para este segundo reto de la semana tu objetivo será incrementar el funcionamiento del programa del día de ayer. Si recordamos, ayer construimos un programa en Python capaz de registrar un nuevo usuario en el sistema. Pues bien, continuando con el proyecto, el reto de hoy será que podremos registrar un N cantidad de nuevos usuarios.

Para esto el programa deberá preguntar cuando nuevos usuarios se pretenden registrar.
Si el por ejemplo coloco 5, bueno, serán 5 nuevos usuarios los que se deben capturar, usuarios con sus correspondientes valores: Nombre, apellidos, número de teléfono y correo electrónico.
Además de todo esto, añadiremos una capa extra de seguridad, implementando un par de validaciones sobre los valores que se pueden ingresar.

Validaremos que, tanto nombre, apellidos como correo electrónico tengan una longitud mínimo de 5 caracteres y un longitud máxima de 50.

Así mismo el número de teléfono será a 10 dígitos.

Si por alguna razón el usuario ingresa mal alguno de estos datos, el programa deberá notificarle y no permitirá continuar hasta que se ingresen datos correctos.

la solucion esta en [main.py](./main.py)