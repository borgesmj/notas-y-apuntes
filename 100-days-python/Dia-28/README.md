# 👉 Desafío del Día 28
Utiliza el generador de personajes del Día 27 para este proyecto... ¡para construir un sistema de batalla automatizado del juego!

Añade funciones de retorno a los estados de salud y fuerza de tu personaje del proyecto del Día 27.
Genera dos personajes diferentes y almacena sus datos (estadísticas de salud y fuerza, tipo de personaje, nombre, etc.).
Utiliza un bucle while True para simular la lucha entre los dos personajes.
Tira un dado de seis caras para ambos personajes. El personaje que saque la mayor cantidad gana esa ronda.
El ganador de esa ronda (el que sacó el número más alto) hará daño al otro personaje haciendo lo siguiente:
Halla la diferencia entre la fuerza de ambos oponentes y súmale uno.
Resta esa cantidad de la salud del perdedor.
Al final de cada ronda, comprueba las estadísticas de cada personaje para asegurarte de que ninguno de ellos ha muerto todavía.
Cuando uno de los personajes muera (se quede sin salud), ¡declara un ganador de la batalla!
Para evitar que esta batalla se vea horrible entre rondas usa time.sleep para hacer una pausa entre rondas os.system("clear") para asegurar que la pantalla se limpia entre batallas.
Puntos extra por el uso de emojis, colores, ¡o incluso código de sonido!

Ejemplo:

```
⚔️ BATTLE TIME ⚔️

Name your Legend:
Arthur the Magnificent
Character Type (Human, Elf, Wizard, Orc): 
Elf

Arthur the Magnificent
HEALTH: 13
STRENGTH: 18

Who are they battling?

Name your Legend:
Sheila the Almighty
Character Type (Human, Elf, Wizard, Orc): 
Human

Sheila the Almighty
HEALTH: 40
STRENGTH: 26

*clear screen here*

⚔️ BATTLE TIME ⚔️

The battle begins!

Arthur wins the first blow
Sheila takes a hit, with 8 damage

Arthur the Magnificent
HEALTH: 13

Sheila the Almighty
HEALTH: 32

And they're both standing for the next round!

*clear screen here*

⚔️ BATTLE TIME ⚔️

The battle continues!

Sheila wins round 2
Arthur takes a hit, with 8 damage

Arthur the Magnificent
HEALTH: 5

Sheila the Almighty
HEALTH: 32

And they're both standing for the next round!

*clear screen here*

⚔️ BATTLE TIME ⚔️

The battle continues!

Sheila wins round 3
Arthur takes a hit, with 8 damage

Arthur the Magnificent
HEALTH: -3

Sheila the Almighty
HEALTH: 32

Oh no Arthur the Mighty has died!

Sheila the Almighty destroyed Arthur the Magnificent in 3 rounds!
```

LA solucion la encuentra en [main.py](./main.py)