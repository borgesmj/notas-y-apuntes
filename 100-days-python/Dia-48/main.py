import os, time

while True:
  time.sleep(1)
  os.system('clear')
  print('🌟HIGH SCORE TABLE🌟')
  f = open("highScores.txt", "a+")
  name = input("Introduce tus iniciales: ")
  score = input("Introduce el puntaje: ")
  f.write(f"{name} {score}\n")
  time.sleep(1)
  os.system('clear')
  print('Añadiendo')
  time.sleep(1)
  os.system('clear')
  print("Añadido")
  time.sleep(1)
  os.system('clear')
  opcion = input('¿Otra entrada?\ns/n > ')
  if opcion == 's':
    continue
  else:
    f.close()
    break
    exit()
  