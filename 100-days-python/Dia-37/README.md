# Cortar Strings
¿No son los string geniales? Si, lo son
Sin embargo, a veces quizas querramos tomar una parte del string para usarlo en alguna parte mas. A veces, podriamos querer mirar justo a la primera letra de un string o cortarlo en pedazos.
Para hacer esto, usamos **string slicing**
Un string no es mas que un monton de texto. De hecho, es una lista de muchos caracteres individuales. Esto significa que podemos usar el `index` como hicimos en la lista el [dia 32](../Dia-32/README.md)
Dandole a nuestro program,a un idex, le estamos diciendo especificamente donde queremos cortar🪓🪓

## Corte
Para cortar un solo caracter desde un string completo, usamos el index de ese caracter dentro de corchetes `[0]` igual como lo hicimos con una lista.

Mira que pasa:

```
myString = "Hello there my friend."
print(myString[0])

# This code outputs the 'H' from 'Hello'
```

Para cortar mas de un caracter, usamos dos indices (que es el plural para index): el caracter donde comienza y uno despues de donde queremos que corte (recordemos que los indices comienzan en 0)

Intentemos:

```
myString = "Hello there my friend."
print(myString[6:11])

# This code outputs 'there'.
# El caracter 0 es H, se comienza a contar desde alli, siendo el 6to caracter la t y el espacio al final de la palabra
```

Dejando el primer index en blanco, por defecto, va a comenzar a contar desde 0:
```
myString = "Hello there my friend."
print(myString[:11])

# This code outputs 'Hello there'.
```

Dejando el segundo index en blanco, va a ir hasta el final del string:

```
myString = "Hello there my friend."
print(myString[12:])
# This code outputs 'my friend.'.
```

## El tercer argumento secreto
Añadiendo un tercer argumento a los corchetes `[ ]` especifica el espacio o saltos entre caracteres:

```
myString = "Hello there my friend."
print(myString[0:6:2])

# This code outputs 'Hlo' (every second character from 'Hello').
# comienza en 0, 'H'
# salta al caracter 2, 'l'
# salta al caracter 4, 'o'
```

¿Puedes imprimir cada tres caracteres de todo el string?

```
myString = "Hello there my friend."
print(myString[::3])

# This code outputs 'Hltrmfe.' (every third character from the whole string).
# Comienza con el caracter 0: 'H'
# Salta 3 espacios: 'l'
# Salta 3 espacios: 't'
# Salta 3 espacios: 'r'
# Salta 3 espacios: 'm'
# Salta 3 espacios: 'f'
# Salta 3 espacios: 'e'
# Salta 3 espacios: 'e'
# Salta 3 espacios: '.'
```

Usando un numero negativo como el tercer argumento puede ser bastante util. Comienza a cortar desde el final en lugar de desde el comienzo

¿Puedes imprimir el string al reves?

```
myString = "Hello there my friend."
print(myString[::-1])

#This code reverses the string, outputting '.dneirf ym ereht olleH'
```
## Split
`Split`nos deja divir un string a una lista individual de palabras, separandolos por espacios en blanco.


## Errores comunes
### ¿Por que imprime 'HEll' en lugar de 'Hello'
```
myString = "Hello there my friend."
print(myString[0:4])
```

Al ser 4 el index siguiente a la ultima letra que el programa va a imprimir, solo ejecutará desde el index 0 hasta el index 3.

```
myString = "Hello there my friend."
print(myString[0:5])
```

### No para de imprimir el mismo caracter
```
myString = "Hello there my friend."
print(myString[0:4:0])
```
El 0 en el tercer caracter significa que "se va a mover 0 posiciones cada vez".
El tercer argumento debe ser, al menos, 1

## Reto del dia
Este es el reto que estás buscando. Este programa generará tu nombre de Star Wars.

1. Pide al usuario que introduzca su nombre y apellidos.
2. Corta las 3 primeras letras del nombre.
3. Corta las 3 primeras letras del apellido.
4. Únelos. Lo ideal es cambiar las mayúsculas y minúsculas para que quede bien - piensa en fStrings o .upper()/.lower(). Este es el nombre de pila de Star Wars del usuario.
5. Ahora pregunta al usuario el apellido de soltera de su madre y la ciudad en la que nació. (El apellido de soltera es el apellido que tenían antes de casarse. Si no estás seguro, invéntate un apellido).
6. Combina las dos primeras letras del apellido de soltera con las 3 últimas letras de la ciudad para formar el apellido Star Wars del usuario. Recuerda, fStrings y .upper()/.lower().
Por último, imprime ambos como parte de una frase.
🥳 Puntos extra por obtener todas las entradas con un solo comando de entrada y la función split.

Ejemplo:

```
🌟Star Wars Name Generator🌟

Input your first name > David

Input your lastname > Morgan

Input your mother's maiden name > Jones

Input the city where you were born > Cardiff

Your Star Wars name is Davmor Joiff
```

La solucion a este reto está en [main.py](./main.py)