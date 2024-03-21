# Gotta Catch 'Em All.... 
### And Put Them In A Dictionary 

Este desafío consiste en utilizar diccionarios para crear un juego sobre pequeñas criaturas que has capturado, esclavizado y obligado a luchar para tu diversión. Tú monstruo.

Este juego no tiene copyright y es totalmente respetuoso con los abogados. ¿Qué pika? No tengo ni idea de lo que quieres decir..... oficial.

# 👉 Desafío del día 42

"Algunos entrenadores no tienen miedo. Para ellos, esto es un reto más".

1. Crea un diccionario para almacenar los detalles de tu, ejem, _MokéBeast_.
2. Pide al usuario que introduzca los siguientes datos: nombre, tipo (tierra, fuego, aire, agua o espíritu), movimiento especial, PV inicial y PM inicial.  Por ahora sólo vamos a introducir un conjunto de valores para una bestia.
3. Introduce los datos de la bestia.
4. Comprueba el tipo de bestia y cambia el color del texto en consecuencia. El fuego es rojo, el agua es azul, el aire es blanco. Los demás los decides tú.

🥳 Puntos extra por conseguir todas las entradas con un solo comando `input` y la función `split`.

👉 INFO IMPORTANTE - anota dónde está este Repl, lo necesitarás dentro de un par de lecciones.

Ejemplo:

```
👾 MokéBeast - El juego genérico de batalla de bestias sin copyright 👾

Introduce el nombre de tu bestia > Brian

Introduce el tipo de tu bestia > Tierra

Introduce el movimiento especial de tu bestia > Flying bellyflop

Introduce los PV de tu bestia > 50

Introduce los PM de tu bestia > 20

# Este texto sale en verde
Tu bestia se llama Brian. Es una bestia de tierra con un movimiento especial de Flying bellyflop
```

<detalles> <sumario> 💡 Pistas </sumario>
  
- Comience con su diccionario.
- Usted necesitará un bucle `for`.
- Cambie el color de fuente para el tipo de la bestia usando `if` declaraciones.
- Cambia el color de la fuente usando `print("\033[XXm", end="")` - sustituye el XX por un [código de color](https://ozzmaker.com/add-colour-to-text-in-python/).
</detalles>