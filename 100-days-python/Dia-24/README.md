# Dia 24: parametros
LO sabemos. Hasta ahora, las subrutinas han sido un poco decepcionantes.

Mejoremos esas subrutinas enviandoles informacion usadno parametros y haciendolas diferentes basadas en sus entradas

Si cambias los ingredientes de una receta, tienes una torta totalmente diferente. Hagamos eso con las subrutinas.

En una subrutina, los `()` están para los argumentos (argunmento es un sinonimo de parametro). Estas son las piezas de informacion que le pasaremos al codigo. Pueden ser nombres de variables que se componen por primera vez dentro del argumento ().

![alt text](../Images/subrutina.png)

Aqui hay una subrutina simple, que usa el argunmento para tomar el nombre de un ingrediente, y expresa su opinion acerca del ingrediente que el usuario ha introducido, 'chocolate' es genial, 'brocoli', no mucho

```
def whichCake(ingredient):
if ingredient == "chocolate":
  print("Mmm, chocolate cake is amazing")
elif ingredient == "broccoli":
  print("You what mate?!")
else: 
  print("Yeah, that's great I suppose...")
```
Ahora, ¿como lo llamamos?

Podemos llamarla de la misma manera que antes. Sin embargo, en vez de dejar los `()` en blanco, le enviaremos al codigo un mensaje

```
whichCake("zanahoria")
```
¿Que pasa si añadimos esta linea al final de nuestro codigo?

¿Que pasa si le colocamos 'brocoli'?

## Añadiendo mas argumentos
Podemos colocar tantos como queramos, separado por comas

Esta subrutnia abajo está esperando tres argumentos: ingredientes, base y cobertura:

```
def whichCake(ingrediente, base, cobertura):
  if ingrediente == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingrediente == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
  print("So you want a", ingrediente, "cake on a", base, "base with", cobertura, "on top?")

whichCake("chocolate", "biscuit", "icing")
```

Incluso podemos preguntarle al usuario que es lo que quiere para su torta utilizando unos `input()`

```
userIngredient = input("Nombra un ingrediente: ")
userBase= input("Nombra un tipo de base: ")
userCobertura = input("Topping favorito: ")
whichCake(userIngredient, userBase, userCobertura)
```

## Errores comunes
### Invalid Syntax
```
def biggerNumber(number1 number2):
  if(number1 > number2):
    print(number 1, "is bigger")
  else:
    print(number 2, "is bigger")

biggerNumber (18,332)
```

Los parametros tienen que estar separados por una coma, y los nombres de las variables sin espacios

## Reto del dia
Crea subrutinas que tiren un dado con cualquier número de caras (esencialmente un número tan grande como quieras). Escribe una subrutina con un parámetro que nos permita llamar a una función (como rollDice).

La solucion la encontramos en [main.py](main.py)