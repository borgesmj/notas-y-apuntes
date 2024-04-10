# 👉 Desafío del día 62

¡Cuidado, Gran Hermano! Hoy es día de proyectos y vas a construir tu propio diario privado para mantener tus pensamientos más íntimos en secreto para el mundo.

Tu diario deberá:

1. Establecer una contraseña de acceso.
2. Pedir al usuario que introduzca una contraseña.
3. Si no aciertan la contraseña, salir del programa.
4. Si la aciertan, entran en el menú principal, que ofrece 'Añadir' o 'Ver' entradas de diario. 
5. Si se elige "Añadir", se debería:
    * Pedir al usuario que escriba la entrada y almacenarla en la base de datos con la marca de tiempo como clave.
6. La opción "ver" debería
    * Mostrar al usuario la entrada anterior (más reciente).
 2. A continuación, puede elegir ver la *siguiente* entrada anterior hacia atrás hasta llegar al final. O volver al menú.


🥳 Puntos extra por añadir una función que permita al usuario ver una entrada a partir de una fecha exacta.

<detalles> <sumario> 💡 Consejos </sumario>

- Usa `if passwordEntered != correctPassword` para verificar el usuario.
- Utilice `os.clear()` para borrar la pantalla entre cada entrada visualizada.
- Puntos extra - compare la fecha introducida con la marca de tiempo y sólo muestre si la fecha introducida >= marca de tiempo.




</detalles>

La solucion la encontramos e [main.py](./main.py)