import os, time


def loadData(itemsData):
  try:
    f = open("inventory.txt", "r")
    itemsData = eval(f.read())
  except:
    itemsData = []  # Si el archivo no existe, simplemente inicializa 'itemsData' como una lista vacía
  return itemsData


def clearScreen(seconds):
  time.sleep(seconds)
  os.system('clear')


def writeFile(itemsData):
  f = open("inventory.txt", "w")
  f.write(str(itemsData))
  f.close()


def addItem(itemsData):
  newItem = input('¿Que items deseas agregar? > ')
  clearScreen(1)
  print(f"Agregando {newItem}...")
  itemsData.append(newItem.lower())
  clearScreen(1)
  print(f"{newItem} agregado.")
  writeFile(itemsData)
  return itemsData


def removeItem(itemsData):
  if len(itemsData) > 0:
    itemToRemove = input('¿Qué item deseas eliminar? > ')
    if itemToRemove.lower() in itemsData:
      clearScreen(1)
      count = itemsData.count(itemToRemove)
      plural_suffix = 's' if count > 1 else ""
      print(
        f"Tienes {count} {itemToRemove}{plural_suffix} en tu inventario\n¿Deseas eliminar uno solo o todos?"
      )
      userInput = input("1. Uno solamente\n2. Todos\n> ")
      if userInput == '1':
        itemsData.remove(itemToRemove)
      elif userInput == '2':
        while itemToRemove in itemsData:
          itemsData.remove(itemToRemove)
    else:
      print('Ese item no se encuentra en el inventario')
  else:
    print(
      'En este momento no hay items en tu inventario\nAñade uno desde el menu inicial'
    )
    print()
    input("Presione ENTER para continuar")
  writeFile(itemsData)
  return itemsData


def viewItems(itemsData):
  if len(itemsData) > 0:
    itemToView = input('¿Qué item deseas ver? > ')
    if itemToView.lower() in itemsData:
      clearScreen(1)
      count = itemsData.count(itemToView)
      plural_suffix = 's' if count > 1 else ""
      print(f"Cuentas con {count} {itemToView}{plural_suffix}")
      input("Presione ENTER para continuar")
    else:
      print('Ese item no se encuentra en el inventario')
      return itemsData
  else:
    print(
      'En este momento no hay items en tu inventario\nAñade uno desde el menu inicial'
    )
    print()
    input("Presione ENTER para continuar")
    return itemsData


def executeApp(itemsData):
  while True:
    clearScreen(1)
    print("🌟Inventario RPG🌟")
    print("1. Añadir Item\n2. Eliminar Item\n3. Mostrar Items")
    userInput = input("> ")
    if userInput == '1':
      itemsData = addItem(itemsData)
    elif userInput == '2':
      itemsData = removeItem(itemsData)
    elif userInput == '3':
      viewItems(itemsData)
    else:
      continue


itemsData = []
itemsData = loadData(itemsData)
executeApp(itemsData)
