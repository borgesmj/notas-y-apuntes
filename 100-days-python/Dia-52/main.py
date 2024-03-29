import os, time


def clearScreen(seconds):
  time.sleep(seconds)
  os.system('clear')


def loadFile(orders):
  try:
    f = open("orderList.txt", "r")
    orders = eval(f.read())
  except FileNotFoundError:
    print("Archivo no encontrado, creando nuevo archivo...")
    orders = []  # Si el archivo no existe, simplemente inicializa 'orders' como una lista vacía
  except Exception as e:
    print("Error al cargar el archivo:", e)
  return orders


def writeFile(taskList):
  f = open("orderList.txt", "w")
  f.write(str(taskList))
  f.close()


def setPrice(typeOfPizza, size):
  pizzas = {
    'Margarita': {
      'grande': 8,
      'mediana': 5,
      'pequeña': 3
    },
    'Napolitana': {
      'grande': 9,
      'mediana': 6,
      'pequeña': 4
    },
    'Hawaiana': {
      'grande': 10,
      'mediana': 7,
      'pequeña': 5
    }
  }
  return pizzas[typeOfPizza][size]


def newOrder(orders):
  clearScreen(1)
  # Preguntar que tipo de pizza quiere el cliente
  print("¿Que pizza vas a ordenar?")
  print("1. Margarita\n2. Napolitana\n3. Hawaiana")
  opcion = input("> ")
  if opcion == '1':
    typeOfPizza = 'Margarita'
  elif opcion == '2':
    typeOfPizza = "Napolitana"
  elif opcion == '3':
    typeOfPizza = 'Hawaiana'

  # Preguntar Cuantas unidadades quiere
  units = 0
  while units == 0:
    units = input(f"¿Cuántas pizzas {typeOfPizza.lower()} vas a ordenar? > ")
    try:
      units = int(units)
      break
    except ValueError:
      print("Debe ser un número entero. Inténtalo de nuevo")
      continue
  print('Elige el tamaño')
  opcion = input("1. Grande\n2. Mediana\n3. Pequeña\n> ")
  if opcion == '1':
    size = "grande"
  elif opcion == '2':
    size = "mediana"
  else:
    size = 'pequeña'

  # Enviar el tamaño y tipo de pizza a una subrutina para que nos regrese
  # el precio al detal
  price = setPrice(typeOfPizza, size)

  # Calculamos el total de la orden
  total = price * units

  # Pedimos el nombre del cliente
  name = input("A nombre de quien realizamos la orden > ")

  # Le imprimimos la factura
  clearScreen(1)
  print(
    f"Gracias por tu compra {name}\nTu orden es {units} pizzas {typeOfPizza} {size} y el total es {total}"
  )
  row = [name, typeOfPizza, units, size, total]
  orders.append(row)
  writeFile(orders)
  input("Presione ENTER para ir al menu inicial")
  return orders


def seeAllOrders(orders):
  clearScreen(1)
  print(f"||{'Nombre':^10} || {'Pizza':^10} || {'Cant.':^5} || {'Tamaño':^10} || {'Total':^5} ||")
  print("============================================================")
  for row in orders:
    print(f"||{row[0]:^10} || {row[1]:^10} || {row[2]:^5} || {row[3]:^10} || {row[4]:^5} ||")
  print()
  input("Para continuar presione ENTER")
  


def createOrders(orders):
  while True:
    clearScreen(1)
    print("🌟Dave's Dodgy Pizzas🌟")
    print("Menu principal\n\n1. Añadir nuevo pedido\n2. Ver todas las ordenes")
    opcion = input("> ")
    if opcion == '1':
      orders = newOrder(orders)
    elif opcion == '2':
      seeAllOrders(orders)
  # break


orders = []
orders = loadFile(orders)
createOrders(orders)