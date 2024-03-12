# Listas

HOy trabajaremos con Listas, es una estructura de datos, utilizando estructuras de datos, podemos almacebar diferentes tipos de dsatos  en secuencia

por ejemplo: 

```
my_list = [1 , 3.14, 'String', True, [2,3.111, 'example', False]]
print(my_list)
print(type (my_list)) # incluso podemos consulta el tipo y nos regresará que es una lista
```

Podemos ver como podemos almacenar distintos tipos de datos, incluso otra lista y lo podemos correr en consola y no deberia tener problemas. Aunque podemos ver que nuestra lista puede almacenar cualquier tipo de dato, es recomendable que las listas tengan un solo tipo de datos
```
courses = ['Python', 'Java', 'C++', 'C#', 'JavaScript']
print(courses)
```
Los elementos que se encuantran almacenados en la lista tienen un indice

```
courses = ['Python', 'Java', 'C++', 'C#', 'JavaScript']
print(courses[0])
# Python
```

Vaya, ya llegamos al reto número 3 de la semana, y para este tercer reto lo que haremos será añadir 2 nuevas funcionalidades a nuestro programa de registro de usuarios.

Estas funcionalidades son las siguientes

1.- Siempre que se registre un nuevo usuario de forma exitosa generaremos un identificador único para este registro/usuario. Te recomiendo sea un ID numérico auto incremental, que comience en 1 hasta N. Sin embargo siéntete libre elegir el formato o tipo que tú desees.

2.- Todos estos nuevos identificadores deberán almacenarse en un listado que será impreso en consola cuando todos los registros se hayan creado. Esto de tal forma que el usuario pueda conocer y tenga certeza que las operaciones, en efecto, se realizaron de forma exitosa.

Con estas 2 nuevas funcionalidades es probable te intuyas como iremos finalizando nuestro programa para el quinto día.

La solucion la encuentras en [main.py](./main.py)