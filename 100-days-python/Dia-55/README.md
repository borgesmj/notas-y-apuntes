# La librería `os`

En la lección de hoy vamos a utilizar la librería `os` para crear carpetas y navegar por ellas.


Anteriormente, hemos usado `os` para limpiar la pantalla.

Aquí hay algunas otras cosas que puede hacer: 

## Listar un archivo

👉 `listdir()` te permitirá listar todos los archivos:

```python
import os

print(os.listdir()) # Lists all the files in the current directory. Useful for checking that a file is in the folder we think it is.

files = os.listdir()
if "quickSave.txt" not in files:
  print("Error: Quick Save not found.")
#Checks if a file is in a directory and outputs an error if not.

```
## Crear una carpeta

👉 Prueba este código con `os.mkdir()`:

```python
import os

os.mkdir("Hello") # Creates a folder called 'Hello'

```
## Renombra un fichero
👉 `os.rename()` toma 2 argumentos: el fichero a renombrar y el nuevo nombre. 

```python
import os

os.rename("myname.txt", "NEW.o") 

```
*Pista: Necesitarías un fichero llamado "minombre.txt" ya cargado en el árbol de ficheros para poder cambiar el nombre del fichero.*

La capacidad de crear y gestionar archivos y carpetas es realmente útil, especialmente para las copias de seguridad.

### ...¡Lo que nos lleva al reto de hoy!

# 👉 Desafío del Día 55

¡Atrás todo el mundo!

f' es la abreviatura de 'file', por supuesto.  ¿Qué creíais que quería decir?

Sacad vuestras mentes de la cuneta, volved y coged vuestra lista de tareas para guardar/cargar automáticamente del [**Día 51**](../dia-51) y usadla aquí.

Su programa debería:

1. Crear una carpeta de copia de seguridad.
2. Crear un nombre de archivo aleatorio.
3. Guarda una copia de los datos en ese archivo.
4. Todo esto debería ocurrir **antes** del guardado automático.


<detalles> <sumario> 💡 Consejos </sumario>

- Utilice una variable booleana `fileExists` establecido en False para almacenar si el archivo ya ha sido creado.
- Utilice `if fileExists` más adelante para comprobar el estado del archivo antes de crear o escribir.
- Utilice la función `os.mkdir()`.

</detalles>


La solucion está en [main.py](./main.py)