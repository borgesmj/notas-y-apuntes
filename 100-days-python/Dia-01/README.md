# dia 1: print()

La funcion *print()* nos imprime lo que tiene dentro de los parentesis en la consola.

## Ejemplo:
print("Hello World")

Las comillas le dicen al comadno que queremos imprimir texto, o "string", 

## ¿Que pasa si queremos imprimir mas texto?

Podemos colocar tantos *print()* como queramos:

```
print("Nosotros")
print("usaremos mas lineas")
print("de codigo")
```

Pero tambien si queremos imprimir varias lineas de texto bajo un solo comando *print()* lo colocamos entre triples comillas ("""), de esta manera:
```
print("""
    Este es un texto
    de multilinea
    creado con un 
    solo comando print()
""")
```

## Errores comunes:

1. Si colocamos 

`Print("What could go wrong?")`

recibiremos este error:

    > Traceback (most recent call last):
    > File "main.py", line 1, in <module>
    > Print("What could go wrong?")
    > NameError: name 'Print' is not defined

esto se debe a que la funcion *print()* es en minuscula en su totalidad

2. Si colocamos

print "Hello Again"

recibiremos este error:

    > File "main.py", line 1
    > print "Hello Again"
          ^
    > SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello Again")?

Esto se debe a que estamos llamando a la funcion sin los parentesis

3. Si colocamos

print(Please work)

recibiremos este error:

    > File "main.py", line 1
    > print(Please work)
                 ^
    > SyntaxError: invalid syntax

Esto se debe a que necesitamos las comillas para que el codigo lo imterprete como string, ya que sin esos lo toma como una variable que, en nuestro caso, no existe.


## Reto:

Arregla este codigo:

print(= MUSIC+ =)
print("> Songs"
Print("> Albums")
print(> Artists")

## Proyecto, dia 1

1. Escribe tu nombre al mundo:
    Utiliza la funcion *print()* para escribir tu `nombre y la fecha del dia de hoy`
       
2. Copia el siguiente texto e imprimelo en una sola funcion:
    ```
   ¡Me estoy inscribiendo en el desafío de 100 días de Python de Replit!
    Me aseguraré de dedicar tiempo todos los días para programar, al menos 10 minutos al día.
    Utilizaré Replit, un increíble entorno de desarrollo en línea, para poder hacer esto desde mi teléfono esté donde esté. ¡No hay excusas para no programar incluso desde el medio de un campo!
    ```
3. Escribe `Hoy me siento...` con un emoji
4. Escribe `puedes seguir mi progreso en  replit.com/@[tunombredeusuario]`

Y le das `Run`
