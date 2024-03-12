# Bucle `For`

un bucle `While`es perfecto de usar cuando no sabemos cuantas iteraciones queremos que se repitan

Si tenemos una idea de cuantas repeticioes hara nuestro bucle, podemos usar el bucle `for` para repetir el codigo exactamente igual que el bucle `while`.

Sin embargo, podemos establecer una variable, condicion de control e incrementar, todo en una misma linea de código.


![alt text](../Images/bucle-for.png)

## Comparemos
Asi es como creamos un contador en un bucle `while`:

```
counter = 0 
while counter < 10:
  print(counter)
  counter += 1
```

Y asi es como hacemos el mismo trabajo, con el bucle `for`:

```
for counter in range(10):
  print(counter)
```

### Range
la funcion `range` crea una lista de numeros en el rango que la creamos. Si le damos solo un numero, va a comenzar en `0`y se movera a un estado donde el numero final sea uno menos que el numero dentro de los parentesis. En el caso anterior, el numero final seria `9`.

```
range(10)
```

Nota: esta variable solo existe durante el bucle, no despues que fué completado.

## Errores comunes:
### Invalid Syntax

¿Que tiene de error aqui?

```
total = 0
for number in range 100:
  total += number
  print(total)
```

Respuesta: el numero 100 no está dentrp de parentesis

### Name error

¿Que tiene de error aqui?
```
for days in range(7):
print("Day", day)
```

Respuesta: la variable declarada es la que se debe llamar a imprimir

## Reto del dia:

Una cosa común que hace la gente es pedir dinero prestado. Cuando la gente devuelve el dinero, paga intereses que se devuelven anualmente y se añaden a la cantidad original que la persona pidió prestada.

Vas a crear una calculadora de préstamos que muestre cuánto dinero debes por un préstamo de 1.000 $ con una TAE del 5% (TAE es la abreviatura de Tasa Anual Equivalente) a lo largo de 10 años.

Esto significa que cada año la cantidad de dinero que debes aumentará un 5%.

¿Cuánto debes en total durante 10 años?

Utiliza un bucle for y una o dos líneas de código en bucle para determinar la respuesta. (Sugerencia: No lo compliques demasiado. Sólo deberían ser unas pocas líneas de código en total).

La solucion la encuentra en [main.py](./main.py)