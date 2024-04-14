# 👉 Desafío del día 65

¡Hoy es día de proyecto! Vas a usar lo que has aprendido sobre OOP (en el Día 64) para almacenar personajes para mi videojuego.

1. Mi juego necesita tener un personaje con nombre, salud y puntos de magia.
2. Necesita que estos valores se configuren cuando se inicializa.
3. Necesita un método para dar salida a estos datos.
4. Debe haber una subclase 'jugador' que herede de personaje y también tenga un número de vidas.
5. El jugador también debe tener un método '¿estoy vivo?' que compruebe el estado del jugador e informe de si está vivo o no.
6. También debería haber una subclase 'enemigo' con 'tipo' y 'fuerza' adicionales.
7. La subclase 'enemigo' debería tener **dos** subclases:
 1. "orco" con un atributo de "velocidad".
 2. vampiro' con un rastreador 'día/noche
8. Instanciar **un** jugador, **dos** vampiros y **tres** orcos. Tú eliges sus nombres.
9. 9. Imprime sus valores.


Ejemplo:

```
🌟Generic RPG🌟

Jugador
Nombre: David
Salud: 100
Puntos Mágicos: 50
Vidas 3
¿Vivo?: Sí

Nombre: Boris Boris
Salud: 45
Puntos Mágicos: 70
Tipo: Vampiro
Fuerza: 3
¿Día/Noche? Noche

Nombre: Rishi
Salud: 70
Puntos Mágicos 10
Tipo: Vampiro
Fuerza: 75
¿Día/Noche? Día

Nombre: Bill
Salud: 60
Puntos Mágicos 5
Tipo: Orco
Fuerza: 75
Velocidad: 90

Nombre: Ted Ted
Salud: 75
Puntos mágicos:40
Tipo Orco
Fuerza: 80
Velocidad: 45

Nombre: Estación
Salud: 35
Puntos Mágicos: 40
Tipo: Orco
Fuerza: 49
Velocidad: 50
```

<detalles> <sumario> 💡 Pistas </sumario>

- Usted sólo necesita heredar de la clase dierctly por encima. Así orco sólo necesita heredar de enemigo, por ejemplo.

</detalles>


La solucion la encontramos en [main.py](./main.py)