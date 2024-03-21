# El Ahorcado

Este sencillo juego es en realidad bastante complejo. Este proyecto del ahorcado combina listas, manipulación de cadenas y troceado, junto con otros conceptos.

Es un poco más complicado, así que no tengas miedo de consultar las pistas y soluciones si te quedas atascado. También puedes consultar nuestro foro [100 Days of Code](https://ask.replit.com/c/100-days-of-code/30) para obtener ayuda.

## Elegir de una lista al azar

👉 `random.choice()` escoge un elemento al azar de una lista.

Aquí tienes una lista de palabras:

```
listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]
```

Para seleccionar al azar de esta lista, asignamos `random.choice()` a una variable.  Le damos a `random.choice()` el nombre de la lista entre paréntesis.

```
listOfWords = ["británico", "suave", "integridad", "acento", "malvado", "genio", "Downton"]
palabraElegida = random.choice(listaPalabras)
```

Hay **muchas** otras cosas necesarias para que este programa funcione, pero, las desglosaremos en la sección _desafío_ del tutorial de hoy.

## Reto del dia:
Una vez elegida la palabra, deben suceder las siguientes cosas:

1. Pedir al usuario que escriba una letra.
2. Comprobar si la letra está en la palabra.
3. En caso afirmativo, muestra la palabra con todos los espacios en blanco excepto la(s) letra(s) que ya ha(n) adivinado.
4. Mantenga una lista de las letras que han utilizado.
5. Cuente cuántas veces han elegido una letra que **no** está en la palabra: más de 6 y pierden.
6. Si revelan todas las letras, aparecerá un mensaje de "ganador".


🥳 Puntos extra por usar [ASCII art](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c) para dibujar el ahorcado mientras el jugador adivina incorrectamente.

Ejemplo:

```
🌟Hangman🌟

Elige una letra: i
No, no está.
Quedan 5.

Elige una letra: a
¡Correcto!
__a__

Elige una letra: s
¡Correcto!
s_a__

Elija una letra: u
Correcto
sua__

# Repetir hasta.....
# Si el usuario gana
Ha ganado con 5 vidas restantes.

# Si pierde
Has perdido
```



La solucion la puede encontar en [main.py](./main.py)