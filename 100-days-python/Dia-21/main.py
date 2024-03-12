import random
# Algunos mensajes aleatorios para mostrar cuando el usuario acierte la respuesta
messages = [
  "Acertaste",
  "Buena reapuesta",
  "DING DING DING"
]


print("""
  Bienvenido a la prueba de Matemáticas

  Podremos a prueba tus conocimientos de 
  multiplicacion:
  1. Seleccionarás un numero a multiplicar
  2. Resolveras las multiplicaciones que te daremos
  3. Recibes un punto por cada respuesta correcta

  ¿Comenzamos?
""")
print()
while True:
    print("Selecciona un numero entre 2 y 10")
    number = int(input("> "))
# Validamos que el numero sea el correcto utilizando White True para que la pregunta se repita hasta que el usuario coloque el numero correcto
    if 2 <= number <= 10:
# Si es correcto, sale del while True
      break
    else:
      print("por favor, selecciona un numero válidp")
print()
score = 0
for i in range(10):
  print(f"{number} x {i+1} = ")
  answer = int(input("> "))
  if answer == number * (i + 1):
    random_index = random.randint(0,len(messages)-1)
    score += 1
    print(messages[random_index])
  else:
    print(f"Te equivocaste, la respuesta era {number * (i + 1)}")
if score == 10:
    print("""
    😲 ¡Eres un genio!!! 
    ¡Acertaste todas! 🎉
    """)
elif score > 6:
    print(f"""Muy bien hecho, sí que sabes de matemáticas.
    Acertaste {score} de 10.""")
else:
  print(f"Debes seguir practicando, solo acertaste {score} de 10")