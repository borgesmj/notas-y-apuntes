# Inventario de videojuegos

¡Ah, sí! Es la hora del clásico sistema de inventario de los juegos de rol.

Tómate una poción de resistencia y dirígete a la página del desafío para conocer todos los detalles.

# Desafío del día 53

El sistema de inventario de tu videojuego debería

1. Tener un menú que permita al usuario:
    1. Añadir
    2. Ver
    3. Eliminar
2. Al añadir un elemento, éste se guarda en un archivo utilizando el modo de captura. Se permiten duplicados.
3. Eliminar un elemento lo borra del fichero.
4. Ver es más complicado. Debería mostrar el nombre del elemento y decirte *cuántos* de esos elementos tienes.
5. Usa auto-guardar y auto-cargar con `intentar... excepto`.


Ejemplo:

```
🌟RPG Inventario🌟

1: Añadir 2: Eliminar 3: Ver > 1

Introduce el objeto a añadir: > Poción de maná
Poción de maná ha sido añadido a tu inventario.

1: Añadir 2: Quitar 3: Ver > 2

Introduce el objeto a eliminar: > Espada
Espada ha sido eliminada de tu inventario.

1: Añadir 2: Quitar 3: Ver > 3

Introduce el objeto a ver: > Manga de mago
Tienes 2 mangas de mago
```

<detalles> <sumario> 💡 Consejos </sumario>

- Utiliza la función `count()` cuando visualices un elemento.

</detalles>

La solucion la encuentras en [main.py](./main.py)