# Dia 35: Reto
Crear un gestor de listas de tareas realmente genial. (Sé que ya hemos hecho esto antes... ¡espera!)

Vamos a actualizar el último gestor de listas de tareas que creamos:

+ Crear un menú donde el usuario pueda ver, añadir o eliminar un elemento.
+ El usuario debe ser capaz de editar el texto de un elemento de la lista también.
+ No permitas que el usuario añada duplicados.
+ Comprueba con el usuario que quiere eliminar un elemento de la lista antes de eliminarlo. (¿Es éste el elemento que realmente quiere eliminar?)
+ Ofrezca al usuario la opción de borrar completamente la lista de tareas. (¡Deberías ser capaz de hacer esto en una línea de código!)

Ejemplo:

```
To Do List Manager:

Do you want to view, add, edit, or remove an item from the to do list?
view

record the video for day 36

Do you want to view, add, edit, or remove an item from the to do list?
remove

What do you want to remove?
record the video for day 36

Are you sure you want to remove this?
yes
```

La solucion la encontramos en [main.py](./main.py)