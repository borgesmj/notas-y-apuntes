# Dia 27: Reto

Bienvenido a tu primera creación de videojuegos. Crearás un videojuego que crea las estadísticas de salud y ataque de un personaje... junto con un nombre épico para tu personaje.

No borres el código de hoy. Lo utilizarás como base el día 28.

+ Escribe una subrutina que genere un personaje: nombre y tipo de personaje (humano, diablillo, mago, elfo, etc.).
+ Escribe una subrutina que multiplique un puñado de tiradas de dados aleatorias para generar las estadísticas de salud del personaje. Usa esta fórmula:

```
6-sided-roll * 12-sided-roll
-----------------------------  + 10
                2
```
+ Escribe una segunda subrutina que multiplique un puñado de tiradas de dados aleatorias para generar las estadísticas de fuerza del personaje.

```
6-sided-roll * 12-sided-roll
-----------------------------  + 12
                2
```

+ Presenta los datos en un menú con time.sleep y os.system("clear") para hacerlo atractivo.
+ Envuélvelo en un bucle para que el usuario tenga la opción de crear otro carácter.

```
Character Builder

Name Your Legend:
Sheila the Almighty

Character Type (Human, Elf, Wiard, Orc):
Human

Sheila the Almighty
HEALTH: 40
STRENGTH: 26

May your name go down in Legend...
```


LA solucion la encontramso en [main.py](./main.py)