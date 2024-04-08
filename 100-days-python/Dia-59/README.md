# A Man A Plan A Canal Panama!


El reto de hoy trata sobre [**palíndromos**](https://es.wikipedia.org/wiki/Pal%C3%ADndromo).

Un palíndromo es una palabra que es simétrica (es decir, que se lee igual al revés que al derecho). 

Por ejemplo:
- racecar
- madam
- radar

Ahora que ya sabes lo que es un palíndromo, vuelve atrás y echa un vistazo al título de esta página. El que te hizo decir, *¿eh?!* ¿Lo tienes ahora? ¡Genial!


# 👉 Desafío del día 59

Vas a escribir un programa que compruebe si una cadena es un palíndromo.

Sí. Sabemos que Python tiene la función `string.reverse()` que puedes usar. 

Cero puntos por eso hoy, queremos que pienses bien y utilices tus habilidades en:
- recursividad
- troceado de cadenas
- bucles

Tu programa debería:

1. Pedir al usuario que introduzca una palabra.
2. Analizar la palabra para ver si es un palíndromo.
3. Emitir un mensaje "sí/no". 


Ejemplo:

```
🌟Comprobador de palíndromos🌟

Introduzca una palabra > Racecar

Racecar es un palíndromo. ¡Sí!
```

<detalles> <sumario> 💡 Pistas </sumario>

Éste es un problema difícil, así que te he dado algunas pistas sobre el pensamiento algorítmico necesario para un problema como éste:
 
- No olvides estandarizar las mayúsculas y minúsculas en la entrada.
- Piensa qué caracteres de una palabra se comparan primero. Comprueba si son iguales.
- Si se han comparado y son iguales, elimínalos y repite el proceso con la cadena más corta.
- Continúe hasta que quede una cadena de longitud 1 ó 0 (dependiendo de si la palabra original tenía un número par o impar de caracteres). Si llegas a este punto, tienes un palíndromo. 

</detalles>