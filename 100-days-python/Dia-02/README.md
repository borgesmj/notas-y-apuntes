# Input y variables

Hoy veremos el comando *input()* y como funciona. *input()* funciona para cuando el usuario le da una informacion al computador.

Es muy similar el comando *print()*, excepto que mostrará un mensaje en la consola y esperará hasta que el usuario haya escrito algo en la consola y haya presionado *Enter*. Vamos a intertarlo:

En el archivo `main.py` escribe el siguiente código

`input("¿Cual es tu nombre?: ")`


La funcion *input()* toma una variable, pero no tiene un sitio donde guardarlo, asi que solucionaremos eso usando una variable, que podemos utilizar para guardar datos

`miNombre = input("¿Cual es tu nombre?: ")`

## Nombrando variables:

Podemos colocar el nombre que queramos a las variables, pero no podemos utilizar espacios:

Tambien podemos utilizar UNO de estos dos sistemas
    + snake_case: separamos las palabras con un guin bajo (_) y todas en minusculas.
    + camelCase: la primera palabra será en minuscula, a partir de la segunda palabra, la primera letra será en mayuscula

Ahora, elimina el código que tienes hasta ahora y coloca  
```
myName = input("¿Cual es tu nombre?: ")
myAge = input("¿Que edad tienes? :")
print("Jeje, eso es bastante viejo")
replit = input("¿Te gusta replit? ")
print("claro que si")
```
## Imprimiendo Variables
Puedes imprimir variables en la consola utilizando el comando *print()*, intentemoslo ahora:
Copia el siguiente codigo, y añadelo al que ya hicimos antes:
```
print()
print("Entonces, tu eres")
print(myName)
print("y tienes la edad de")
print(myAge)
print("y claramente lo que piensas de replit es:")
print(replit)
```

¿Notaste que pasa si escribimos *print()* sin nada entre loa parentesis?
La consola imprime una linea en blanco

## Errores Comunes
Borra todo el código que tenemos hasta ahora, y copia cada código para que veas el error:

### Syntax Error
```
my variable = input("WHO GOES THERE? ")
print(my variable)
```

```
  File "main.py", line 1
    my variable = input("WHO GOES THERE? ")
       ^
SyntaxError: invalid syntax
```

Esto se debe a que las variables no deben tener espacios, utiliza camelCase o snake_case para nombrar una variable

### Name Error

```
myGrandma = input("How's your Grandma doing? 😘 ")
print(mygrandma)
```

```
How's your Grandma doing? 😘 fine
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    print(mygrandma)
NameError: name 'mygrandma' is not defined
```

Esto se debe a que la variable la nombramos de una manera y la llamamos a imprimir con otro nombre, y basicamente estamos llamando a una variable inexistente

### Esto se puso un poco raro

```
myLunch = input("What are you having for lunch? ")
print("Hmm, it sounds like you really should just order")
print("myLunch")
print("as soon as possible!")
```

```
What are you having for lunch? Burrito
Hmm, it sounds like you really should just order
myLunch
as soon as possible!
```
Este codigo funciona, pero no me dice lo que comeré de almuerzo, ¿por qué?
Porque estoy llamando a imprimir "myLunch" como un string mas no como una variable, para solucionar esto, debemos quitar las comillas (")

## Arregla este codigo

```
print("Definitely not a Phishing Scam")
print()
input("Your Name")
print("Thanks for logging in")
print(myName)
cardNumber = input("What is your credit card number?")
print("Thanks, I definitely wont put")
print("cardNumber")
print("into Amazon and order anything weird")
print()
print("Promise")
maidenName input("What is your Mother's maiden name? ")
print()
print("That's cool, I just wanted to know that")
print(maidenName)
print("was your Mum's maiden name. Not because the bank requested it or anything, honest.")
```

LA solucion la veras en [el codigo](./main.py)


