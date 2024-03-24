¡# Ta Daaaa! Es un To Do

Hoy es un sistema de gestión de listas de tareas. Espera, ¿hemos hecho esto? Sí, pero tu última lista de cosas por hacer no te permitía almacenar fechas ni nada aparte de la lista en sí.

Tu programa almacenará una lista de tareas pendientes, y te permitirá dar a cada tarea una prioridad.

Entonces, ¿a qué esperas? Punto 1, máxima prioridad. Visita la página del reto para más detalles.

### ¿Aún aquí? ¡Deja de procrastinar!

# 👉 Reto del Día 45

¿Lo has conseguido? Bien. Pongámonos manos a la obra.

Su sistema debe:

1. Tener un menú que te pregunte si quieres añadir, ver, mover o editar una 'tarea pendiente'.
2. Si eliges "añadir", el sistema debería
   * Pedirte que introduzcas la tarea, el plazo de entrega y la prioridad (alta, media o baja).
   * Añadir la tarea a la lista.

3. La opción "Ver" debería ofrecer dos opciones:
    * Ver todo: muestra todos los 'pendientes' con una bonita impresión.
    * Ver prioridad - permite buscar por prioridad alta, media o baja y **sólo** ver las tareas coincidentes.
4. 'Editar' le permite cambiar cualquier información dentro de una de las 'tareas pendientes'.
5. "Eliminar" le permite eliminar completamente una "tarea pendiente" cuando está "por hacer".




Ejemplo:

```
🌟Organizador de vida🌟

Bienvenido al organizador de vida. ¿Quieres añadir, ver, editar o eliminar una tarea pendiente? > Añadir

¿Cuál es la tarea? > Paga más a los profesores.
¿Para cuándo es? > 11/01/2022
¿Cuál es la prioridad? > Alta

Gracias, esta tarea ha sido añadida.

¿Quieres volver a ver el menú o salir? > Salir.
```

<detalles> <sumario> 💡 Consejos </sumario>

- Usa una subrutina distinta para añadir, ver, editar y eliminar.

- Borrar la consola antes de ver una nueva entrada.

- Utiliza un bucle `while True` para llamar a las subrutinas y mostrar el menú.


</detalles>

LA solucion la encuentra en [main.py](./main.py)