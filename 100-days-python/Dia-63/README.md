# Múltiples archivos

A estas alturas, habrás escrito programas bastante grandes con montones de líneas de código.

Esto puede llegar a ser bastante engorroso de manejar. Mucho desplazamiento para encontrar la parte correcta...

Una de las maneras de superar esto es dividir el código en varios archivos.

Así es. Tus programas pueden consistir en más de un archivo python. El archivo **main** siempre se ejecutará primero, pero puedes poner partes de tu código en otros archivos y traerlos a **main.py** mediante **importación**. 

De hecho, esto ya lo has hecho siempre que has usado `import random`, `import time`, `import os` y demás. Sólo que en esas ocasiones, estabas importando código escrito por otra persona. 

Hoy, crearás tu propio archivo de código y lo importarás a tu programa principal.

👉 Empecemos con un programa básico de 'contar hasta 10' en el archivo `main.py`.

```python
for i in range(10):
  print(i+1)
```

👉 Ahora vamos a moverlo a un nuevo archivo. 

En el menú **files** de la barra de herramientas de la izquierda, busca el icono 'New file' y selecciónalo.

![](recursos/01_archivos1.png)

Nombra el archivo **test.py** - DEBES** incluir el *.py* para especificar que es un archivo python.

![](recursos/01_archivos2.png)



Corta y pega el código de **main.py** en **test.py**.

![](recursos/01_archivos3.png)

A estas alturas, tu archivo **main.py** no debería tener nada.

👉 Ahora haz clic en 'ejecutar'. ¡Mira con asombro *como no pasa nada*!

Recuerda, Python ejecuta el código en el archivo **main.py**, que de momento está vacío. Así que necesitamos importar el código.

👉 Ve a tu fichero **main.py** y añade este código.


```python
import test # No hace falta el .py
```
👉 Ahora ejecuta el código y observa cómo se ejecuta el programa 'cuenta hasta 10'.

## ¿No puede ser tan fácil? ¿Verdad?

Bueno....... no. Porque no podemos controlar **cuando** se ejecuta el programa 'cuenta hasta 10'. Simplemente se ejecuta al importarlo. En este ejemplo, se ejecutaría *antes* que el código `print("Countdown")`. No es lo ideal.

```python
import test

print("Countdown")
```
Para solucionar esto, necesitamos pensar más como bibliotecas. Consisten en un montón de subrutinas que podemos importar y luego **llamar sólo cuando las necesitemos**.

👉 De vuelta en tu archivo **test.py**, necesitas hacer que el programa de cuenta atrás sea una subrutina.

```python
def countdown():
  for i in range(10):
    print(i+1)
```

👉 Por último, vamos a llamarlo en nuestro fichero **main.py**.

```python
import test

print("Countdown")
test.countdown() # Test refers to the file, countdown to the subroutine in that file.
```

### ¡Pruébalo!

# Seudónimos

Si el nombre de tu archivo es realmente largo, puedes darle un pseudónimo, o apodo, como creo que los jóvenes de moda los llaman estos días. Esto te ahorrará tiempo cada vez que quieras ejecutar una subrutina desde ese fichero.

👉 Usa `as` para apodar tu archivo. Aquí he usado `tt` para el archivo `test`. 

``python
import test as tt

print("Countdown")
tt.countdown()
```

### ¡Pruébalo!

# 👉 Reto del día 63

El reto de hoy es convertirte en tu propio bibliotecario. ¡Oook!

En el mundo real, los programadores suelen mantener una biblioteca de sus subrutinas más útiles como ésta. Vas a curar tu propia biblioteca con estas subrutinas.

1. Revisa tus programas y elige algunas subrutinas que hayas usado *mucho*. Tal vez fue tu rodillo de dados. Podría ser tu prettyPrint. Tal vez fue tu subrutina 'generar insulto calvo al azar'. Lo que sea. Encuéntralas.
2. Crea un nuevo archivo que contenga todas tus mejores subrutinas.
3. Importa este archivo a tu main.py y llama a unas cuantas para demostrar que funciona.

<detalles> <sumario> 💡 Pistas </sumario>

- ¡Ya eres mejor que esto! ¡Hoy no hay pistas, amigos! ¡Mucha suerte!

</detalles>

La solucion la tenemos en [main.py]