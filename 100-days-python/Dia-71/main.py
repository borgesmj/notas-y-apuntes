import os, time, random
from replit import db


def clearScreen(seconds):
  time.sleep(seconds)
  os.system('clear')


def addNew():
  clearScreen(1)
  print('Ingresa un nuevo usuario')
  username = input('username > ')
  password = input('password > ')
  salt = random.randint(1000, 9999)
  newPassword = hash(f"{salt}{password}")
  db[username] = {
    'salt': salt,
    'password': newPassword
  }

def login():
  clearScreen(1)
  if len(list(db)) > 0:
    print(list(db))
    username = input('Ingrese su username > ')
    if username in list(db):
      password = input('Ingrese su contraseña > ')
      newPassword = hash(f"{db[username]['salt']}{password}")
      print(newPassword)
      print(db[username]['password'])
      input()
      if newPassword == db[username]['password']:
        print('Bienvenido')
      else:
        print('contraseña incorrecta')
    else:
      print('Usuaio no encontrado')  
  else:
      print('no hay usuarios registrados')


while True:
  clearScreen(1)
  print('🌟Login System🌟\n\nMenu inicial\n1. Añadir nuevo usuario\n2. Login')
  userInput = input('> ')
  if userInput == '1':
    addNew()
  elif userInput == '2':
    login()
  else:
    continue