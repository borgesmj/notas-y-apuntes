import requests
import time, os
from replit import db


def clearScreen():
  time.sleep(1)
  os.system('clear')


def generateJoke():
  results = requests.get("https://icanhazdadjoke.com/",
                         headers={"Accept": "application/json"})
  joke = results.json()
  newJoke = {"text": joke["joke"], "id": joke["id"]}
  return newJoke


while True:
  clearScreen()
  print("Bienvenido al generador de Dad jokes")
  print("""
    Opciones:
    1. Generar un chiste nuevo
    2. Ver los chistes almacenados
    3. Salir del programa
  """)
  opcion = input("> ")
  if opcion == "3":
    exit()
  elif opcion == "1":
    while True:
      clearScreen()
      newJoke = generateJoke()
      print(newJoke['text'])
      print("")
      print("¿Que desea hacer?")
      print("""
        1. Almacenar este chiste
        2. Generar un chiste nuevo
        3. Ir al menu principal
          """)
      opcion = input("> ")
      if opcion == "1":
        clearScreen()
        print("Guardando chiste en la base de datos.")
        clearScreen()
        print("Guardando chiste en la base de datos..")
        clearScreen()
        print("Guardando chiste en la base de datos...")
        db[newJoke["id"]] = newJoke["text"]
        clearScreen()
        print("Chiste almacenado")
        break
      elif opcion == "2":
        continue
      elif opcion == "3":
        break
      else:
        print("opcion incorrecta")
        continue
  elif opcion == "2":
    clearScreen()
    print("Esta es la lista de chistes guardados:")
    keys = db.keys()
    for index, key in enumerate(keys):
      print(f"{index+1}. {db[key]}")
      print()
    print()
    input("presione ENTER para continuar...")
  else:
    print("opcion incorrecta")
