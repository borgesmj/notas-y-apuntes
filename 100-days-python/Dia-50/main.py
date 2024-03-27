import os, time, random


def checkFile(fileName):
  return os.path.exists(fileName)


def openAndWrite():
  f = open("my.ideas", "a+")
  clearScreen(1)
  newIdea = input("¿Que idea tienes ahora?\n> ")
  f.write(f"{newIdea}\n")
  clearScreen(1)
  print("Añadiendo nueva idea")
  clearScreen(2)
  print("Nueva idea añadida")
  f.close()


def openAndRead():
  newData = []
  fileExists = checkFile("my.ideas")
  if fileExists:
    f = open("my.ideas", "r")
    newData = f.read().split("\n")
    f.close()
    return newData
  else:
    f = open("my.ideas", "w")
    f.close()
    return newData


def clearScreen(seconds):
  time.sleep(seconds)
  os.system('clear')


def seeAllIdeas(data):
  clearScreen(1)
  print("Lista de todas las ideas:\n\n")
  for index, idea in enumerate(data):
    if idea != "":
      print(f"{index + 1}. {idea}")
  input("presione ENTER para continuar")


def seeOneIdea(data):
  clearScreen(1)
  index = random.randint(0, len(data) - 2)
  print(data[index])


while True:
  clearScreen(1)
  print("🌟Almacea tu idea🌟\nNo pierdas tu idea de vista")
  print(
    "\nMenu Inicial\n1. Añadir una idea nueva\n2. Ver todas las ideas\n3. Ver una idea aleatoria\n4. Salir"
  )
  option = input("> ")
  if option == '1':
    openAndWrite()
  elif option == "2":
    data = openAndRead()
    if data[0] != '':
      seeAllIdeas(data)
    else:
      print('no hay ideas almacenadas')
  elif option == '3':
    data = openAndRead()
    if  data[0] != '':
      seeOneIdea(data)
    else:
      print('no hay ideas almacenadas')
  elif option == '4':
    clearScreen(1)
    print('adios')
    clearScreen(2)
    break
  else:
    continue
