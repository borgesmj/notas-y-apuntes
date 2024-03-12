# Dia 10: Un poco de matemática

HAsta ahora hemos aprendido a introducir en la computadora dos tipos de numeros:

+ `float`: numeros con decimales
+ `int`: numeros enteros
Copia el codigo abajo y mira las operaciones

 ```
 adding = 4 + 3
 print(adding)

 subtraction = 8 - 9
 print(subtraction)

 multiplication = 4 * 32
 print(multiplication)

 division = 50 / 5
 print(division)

 # a number raised to the power of some number
 # in this example we raise 5 to the power of 2
 squared = 5**2
 print(squared)

 # remainder of a division
 modulo = 15 % 4
 print(modulo)

 # whole number division
 divisor = 15 // 2
 print(divisor)
 ```

 ## Arregla este codigo

 Borra el codigo que tenemos hasta ahora, copia y pega el siguiente codigo y verifica donde estan los errores, solucionalos

 ```
 👉 # Solve the following problems with my code
 # Your goal is to print the solution of all 3 calculations to the screen.

 # multiplication
 3.4 * 6.8

 # division
 2467 / 4673

 #raise 10 to the power of 2

 # print the remainder when 343 is divided by 4
 print("343 // 100")
 ```

 ### Solucion:

 ```
 # 👉  Solve the following problems with my code
 # Your goal is to print the solution of all 3 calculations to the screen.

 # multiplication
 print(3.4 * 6.8)

 # division
 print(2467 / 4673)

 #raise 10 to the power of 2
 print(10**2)
 # print the remainder when 343 is divided by 4
 print(343 // 100)
 ```

 ## Dividamos la cuenta
 ¿Te divertiste con todos esos simbolos matematicos?, pongamoslo en buen uso:

 > Tu y tus amigos fueron a cenar y necesitan dividir la cuenta. Siendo el amigo mas inteligente que eres, usas tu codigo para saber cuanto le toca a cada uno. Recuera que `myBill` es un float y probablemente tenga decimales y `numberOfPeople` es un int porque no vas a cenar coin dos personas y media.


Copia y mira que pasa:

```
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
print("You all owe", answer)
```

¿Recibiste un numero con muchos decimales?

Puedes tomar tu resouesta y usar `round`. Round tiene dos componentes:
1. ¿Que estoy redondeando?
2. ¿A cuantos decimales lo quieres redondear?

Ahora añade esta porcion de codigo a la respuesta y mira que sucede:

```
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = round((myBill / numberOfPeople), 2)
print("You all owe", answer)
```

puede ser de esta manera, o de esta:

```
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)
```

## REto del dia 10
Extiende tu calculadora de cuenta:
Añade una funcion que sume la propina total antes de calcular la parte de cada quien
1. Pregunta al usuario el total de la cuenta
2. Pregunta cual es el % de propina que dejaran para añadirlo a la cuenta total
3. Ingeniatelas para poder ver cuanto es la propina y entonces añadelo al monto original
4. Pregunta al usuario entre cuentas personas será dividida la cuenta

La solucion la tendras en [main.py](./main.py)