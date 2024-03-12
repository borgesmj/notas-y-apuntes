# Tuplas y diccionarios

## Tuplas

Tanto las tuplas como los diccionarios son estructiras de datos, a traves de estar estructuras vamos a almacenar todo tipo de datos, podemos almacenar string, int, float, incluso tuplas y listas

Todas estas estructuras Se rigen bajo un indice,la diferencia es que las listas son mutables, puede ampliar su longitud, mientras que las tuplas son inmutables. Una tupla practicamente es una lista pero inmutable.


Por ejemplo:

```
# tupla 
# la tupla se hace con ()


settings = ( 'localhost', 3306, 'root', 'password', 'database')
print(settings) ##print(type(settings))
print(type(settings)) ##print(type(settings))
print(len(settings)) # 5
print(settings[3]) # password

sub_settings = settings[::-1] # invertir el orden de la tupla para hacer una sub-tupla

print(sub_settings) #('database', 'password', 'root', 3306, 'localhost')

```

Las tuplas solo se utilizan para lectura, no se pueden modificar, no se pueden borrar ni agregar elementos a la tupla. Uno como programador podria pensar que son innecesarias pero es por su misma naturaleza que las hace importante porque los elementos no se van a modificar por lo tanto son seguros.

Investigar desempaquetado de tuplas

## Diccionarios

Al igual que con las listas y las tuplas, son estucturas de datos, se pueden almacenar una *n* cantidada de datos, la diferencia del diccioanrio y las listas o tuplas es que estas ulñtimas trabajan con indices, en cambio los diccionarios trabajan con pares `llave-valor`

### Metodos de diccionario
#### Keys 
```
user = {
  'name': 'Miguel',
  'age': 32,
  'email': 'correo@correo.com',
  'active': True
}

print(user.keys()) ## dict_keys(['name', 'age', 'email', 'active'])
```

#### Values
```
user = {
  'name': 'Miguel',
  'age': 32,
  'email': 'correo@correo.com',
  'active': True
}

print(user.values()) ## dict_values(['Miguel', 32, 'correo@correo.com', True])
```

#### items
```
user = {
  'name': 'Miguel',
  'age': 32,
  'email': 'correo@correo.com',
  'active': True
}

print(user.items()) ## dict_items([('name', 'Miguel'), ('age', 32), ('email', 'correo@correo.com'), ('active', True)])
```

## Reto del dia 
Ya nos encontramos en la recta final de nuestra semana, y lo que haremos ahora, cómo ya es costumbre, será añadir más funcionalidades a nuestro programa.

Puntualmente 4 nuevas funcionalidades. Aquí van.

1.- Ahora todos los valores que representan a un usuario: Nombre, apellidos, número de teléfono y correo electrónico deberán almacenarse en un diccionario.

2.- Se añadirá la opción de poder listar el ID de todos los usuarios registrados hasta el momento.

3.- Se añadirá la opción de poder ver la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este conocer la información registrada.

4.- Se añadirá la opción de poder editar la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este el programa pedirá nuevamente los valores de un registro para actualizarlos.

Estas 3 nuevas opciones deberán ser presentadas al usuario al comienzo del programa, esto con la finalidad que sea el usuario quien defina que quiere hacer justo ahora: añadir nuevos usuario, consultarlos o editarlos.

De igual forma el programa tendrán una quinta opción que le permita la usuario finalizar el programa cuando él lo desee.

Un Tip. Para estas nuevas opciones puedes presentarle a tu usuario un pequeño menú del cual pueda elegir. Por ejemplo opción A.-) registrar nuevos usuarios, opción B.-) listar usuarios, Opción C.-) Editar usuarios y así sucesivamente.

La solucion estará en [main.py](./main.py)