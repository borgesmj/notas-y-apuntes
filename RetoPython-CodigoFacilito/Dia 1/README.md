# Reto Python
## Dia 1
### variables 
#### tipos de datos

nombre_de_la_variable = valor
utilizar snake_case
Nota: no se puede empezar con un numero
```
first_name = 'Miguel'

```

Puntualmente en este ejemplo, el nombre de la variable es first_name, y el valor de la 

variable es "Miguel" y tipo de variable es un string

```
print(first_name)

```

Delarando una variable nueva:
```
last_name = 'Borges'

```
### concatenar
```
print(first_name+last_name) #concatenar sin espacios
print(first_name, ' ', last_name) #concatenar con espacios añadidos manualmente
print(first_name, last_name) #concatenar con espacios añadidos automaticamente
```

### Tipos de variables

  1. int => numero entero
  2. float => numero decimal
  3. string => cadena de texto
  4. boolean => True o False
```
age = 30 #entero
score = 7.8 #float
name = 'Miguel' #string
is_active = True #boolean

print(age)
print(score)
print(name)
print(is_active)

```

Para saber el tipo de variable, tenemos el comando *type()*, dentro de los parentesis colocamos la variable de la que queremos saber el tipo, y todo esto lo almacenamos en otra variable, de esta manera:
```
result = type(age)
print(result)
# <class 'str'>
```

Python es un lenguaje con tipado dinámico, no es de tipado estricto como TypeScript

### Funcion input()

La función input se utiliza para solicitarle al usuario una informacion, y el programa no continuará hasta que el usuario lo haga

La funcion input va a almacenar todo la informacion que el usuario escribi{o hasta que presionó *enter*, y la funcion almacenará como un string

Podemos almacenar toda esa informacion en una variable para poder usarlo luego

```
result = input ()
print(result)
```

```
result = input('ingresa un texto: ')
print('El texto que ingresaste fue =>', result)
```



## Reto del dia
Para este primer reto de la semana, tu objetivo será poder crear un programa en Python el cual permita registrar a un usuario en el sistema.

Para ello el programa deberá pedir a nuestro usuario final ingrese su siguiente información.
Nombre(s)
Apellidos
Número de teléfono
Correo electrónico.

Una vez el usuario haya ingresado todos los datos vía teclado, el programa le dará la bienvenida al usuario con el siguiente mensaje:
Hola + seguido del nombre completo del usuario +, en breve recibirás un correo a + seguido del correo electrónico.

La solucion la encuentras en [main.py](./main.py)
