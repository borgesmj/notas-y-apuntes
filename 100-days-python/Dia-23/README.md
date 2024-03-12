# Dia 23: subrutinas
Hasta ahora, cuando hemos querido repetir codigo, hemos tenido que usar bucles o copiar y pegar codigo
¿Que tal si te digo que hay una manera de usar codigo o llamarlo y usarlo cuando sea donde sea?
Eso es una subrutina
Una subrutina le dice al computador que un pedazo del código existe y que vaya directo a ese codigo una y otra vez.

## Asi como una receta

LAs subrutina trabajan como una receta en un libro de cocina. Si tu quieres sabeer como hacer una torta, no tienes que comenzar de cero cada vez. Puedes usar una receta para que tengan la misma calidad cada vez que se haga.

## ¿Como definimos una subrutina?
Una subrutia se defina con:

```
def (que quiere decir definicion)
```

Tienes que darle a la subrutina un nombre (y asi como a una variabe, no puede tener espacion)

![alt text](../Images/subrutina.png)

Tienes que añadir un `()` incluso si no hay argumentos, seguido por dos puntos `:`. El codigo debe tener sus espaciados.

## Intentemoslo
Lancemos un dado, que nos regresa un numero comprendido por uno de sus 6 lados:

```
def rollDice():
    import random
    dice = random.randint(1, 6)
    print("You rolled", dice)
```

¿Por que no pasa nada?
En este código, hemos definido como se lanza el dado, pero no esta siendo realmente 'llamado' a ejecutar

## Llama a la subrutina
LLamar a la subrutina es decirle al computador que lo ejecute
Necesitamos 'llamar' el codigo añadiendo una linea mas con el nombre de la subrutina y un `()` vacio.

```
def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)

rollDice()
```

> Tienes que asegurarte que cuando llamas a la subrutina NO ESTÉ con espaciado.

NO nos podemos imaginar si añadimos un `range()` para lanzar el dado 100 veces.

```
for i in range(100):
  rollDice()
```

👉 Intentalo

## Errores comunes
### Name error
¿Por que no funciona este codigo?

```
def print My Name():
  print("My Name is David")

print My Name()
```

Los nombres de las subrutinas, al igual que lkas variables, no deben tener espaciado (utiliza camelCase o snake_case)

### Syntax error
¿Por que no funciona este codigo?
```
def countToFive:
  for i in range(1, 6):
    print(i)

countToFive()
```
Necesitas añadir un `()` e n la primera linea, incluso si no hay argumento

### ¿Y que tal este?
```
def countToFive():
    for i in range(1, 6):
      print(i)
    
    countToFive()
```
Las llamadas a las subrutinas no deben tener espaciado.

## Reto del dia:
1. Crea una subrutina con username y password
2. crea un bucle que le pida al usuario login una y otra vez hasya que lo haga correcto

La solucion la encuentras en [main.py](./main.py)