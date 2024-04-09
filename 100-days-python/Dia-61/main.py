import datetime, os, time
from replit import db # Esta libreria solo se puede usar dentro de replit.com

def clearScreen(seconds):
  time.sleep(seconds)
  os.system('clear')

def seeAll():
  clearScreen(1)
  keys = db.keys()
  totalTweets = len(keys) # creamos una variable con la longitud del diccionario
  if totalTweets == 0: # si es 0 le indicamos al usuario que debe añadir uno desde el menu
    print('no hay tweet agregado. Añade uno desde el menu inicial')
    input('Presione ENTER para ir al menu inicial')
    return  
  #vamos a mostrar de 10 en 10
  tweets_per_page = 10
  currentPage = 1

  while True:
    startIndex = (currentPage - 1) * tweets_per_page # index inicial
    end_index = startIndex + tweets_per_page
    current_tweets = list(keys)[startIndex:end_index]
    clearScreen(1)
    for key in current_tweets:
      print(f"[{key}]: {db[key]}")

    if totalTweets <= tweets_per_page:
      input('Presione ENTER para ir al menú inicial')
      break

    print("\n1. Ver 10 tweets más\n2. Ir al menú inicial")
    option = input("> ")
    if option == '1':
      currentPage += 1
      if totalTweets <= currentPage * tweets_per_page:
        currentPage = totalTweets // tweets_per_page + 1
    elif option == '2':
      break
    else:
      print("Opción inválida. Por favor, seleccione una opción válida.")
 
    
  
def deleteAll():
  keys = db.keys()
  for key in keys:
    del db[key]


def addNew():
  clearScreen(1)
  userTweet = input("¿En qué estas pensando?\n> ")
  timestamp = round(datetime.datetime.now().timestamp())
  db[timestamp] = userTweet

while True:
  clearScreen(1)
  print("Twitter clon")
  print("menu inicial")
  print("1. Añadir nuevo tweet\n2. Ver todos los tweets\n")
  userOption = input("> ")
  if userOption == '1':
    addNew()
  elif userOption == '2':
    seeAll()
  elif userOption == 'borrar_todos':
    deleteAll()
