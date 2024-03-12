# Dia 5: Declaraciones "if"

## Declaraciones if

Estas declaraciones son como hacer una pregunta. Le esás diciendo a la computadora que si esa pregunta es cierta, debe realizar algo que coloquemos en un bloque de código. El doble iguel (==) le dice a la computadora que comprae si las dos cosas son *exactamente* iguales.

En el siguien codigo, le preguntamos al usuario su nombre

```
myName = input('¿Cual es tu nombre? ')
if myName == 'David':
```
Esta fraccion de código nos dará error, porque le estamos colocando un "if" pero no le decimos que hará si esa condición es cierta.

```
myName = input('¿Cual es tu nombre? ')
if myName == 'David':
    print('Bienvenido, amigo')
```
## Declaraciones else

¿Y que tal si la condición no se cumple? <br/>
Si la condición no se cumple, entra el juego la declaracion *else*.<br/>
Si la condicion *if* se cumple, la declaracion *else* se ignora.<br/>

```
myName = input('¿Cual es tu nombre? ')
if myName == 'David':
    print('Bienvenido, amigo')
else:
    print('¿Quien eres tú?')
```

> Hay que tener en cuenta los niveles de tabulaciones y puntos: 
> Luego de la declaracion *if* o *else* va dos puntos (:) y en la siguiente linea, si se cumple (o no) la condicion, lleva una tabulacion

### Errores comunes

#### Syntax Error

¿Que hay de malo en este codigo?
```
catsOrDogs = input("¿Eres una persona de gatos o de perros?: ")
if catsOrDogs = "gatos":
  print("Meow")
else:
  print("Woof")
```

> **Respuesta:** falta un simbolo de igual al colocar la declaracion *if*:  `if catsOrDogs = "gatos":`

#### Syntax Error (otra vez)

¿Que hay de malo en este codigo?
```
catsOrDogs = input("¿Eres una persona de gatos o de perros?: ")
if catsOrDogs == "gatos"
  print("Meow")
else:
  print("Woof")
```

> **Respuesta:** falta los dos puntos (:)  `if catsOrDogs == "gatos"

#### Indentation Error

¿Puedes ver el error aqui?

```
catsOrDogs = input("¿Eres una persona de gatos o de perros?: ")
if catsOrDogs == "gatos":
  print("Meow")
else:
print("Woof")
```
> **Respuesta:** falta la tabulación. Tan pronto veamos los dos puntos (:) la siguente linea debe tener una tabulacion de uno.


### Reto del dia:

Vamos a:
1. Preguntar una serie de preguntas al usuario para ver si son un personaje que hayamos creado
2. Añade muchas preguntas *if* como nos sea posible
3. Aseguremosnos de imprimir algo al final en caso de que el usuario no haya elegido a ninguno

> La solucion estara en [main.py](./main.py)
