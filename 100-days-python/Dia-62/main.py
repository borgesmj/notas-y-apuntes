from replit import db
import os, time, datetime
from getpass import getpass


def addNewEntry():
  newEntry = input('¿Que quieres guardar?\n> ')
  timestamp = round(datetime.datetime.now().timestamp())
  db[timestamp] = newEntry


def seeAllEntries():
  keys = db.keys()
  if len(list(keys)) == 0:
    print(
      'Aun no hay entradas en tu diario privado, intenta agregar la primera desde el menu inicial'
    )
    print()
    input('presione ENTER para continuar')
  else:
    index = 0
    while True:
      keys = list(keys)
      keys_sorted = sorted(keys, reverse=True)
      key = keys_sorted[index]
      time.sleep(1)
      os.system('clear')
      print(f"[{key}]: {db[key]}")
      print()
      print('¿Ver siguiente?')
      userOption = input('s/n >')
      if userOption == 's':
        if index >= len(keys_sorted) - 1:
          print('ya no hay mas entradas')
          break
        else:
          index += 1
      else:
        break


def exitProgram():
  print('adios')
  time.sleep(1)
  os.system('clear')
  exit()


def borrarTodo():
  keys = db.keys()
  for key in keys:
    del db[key]


def menuPrincipal():
  while True:
    time.sleep(1)
    os.system('clear')
    print(
      'Menu Principal\n\n1. Añadir nueva entrada\n2. Ver todas las entradas\n3. Salir'
    )
    userInput = input('> ')
    if userInput == '1':
      addNewEntry()
    elif userInput == '2':
      seeAllEntries()
    elif userInput == '3':
      exitProgram()
    elif userInput == '4':
      borrarTodo()
    else:
      continue


def login():
  print('Ingrese su contraseña')
  password = getpass('> ')
  if password == 'mypassword':
    print('Bienvenido usuario')
    menuPrincipal()
  else:
    print('Contraseña incorrecta.')
    exitProgram()


login()