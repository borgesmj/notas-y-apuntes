import os, time


def clearScreen(seconds):
  time.sleep(seconds)
  os.system('clear')


def addTask(todoList):
  clearScreen(0.5)
  print("Añadir nueva tarea")
  row = []
  task = input('¿Cual es la tarea?\n> ')
  row.append(task)
  dueDate = input(
    '¿Cual es la fecha de entrega?\nEl formaro es dd/mm/YYYY\n> ')
  row.append(dueDate)
  opcion = input(
    '¿Cual es la prioridad?\nEscriba el numero de la opción\n1. Alta\n2. Media\n3. Baja\n> '
  )
  if opcion == '1':
    priority = 'Alta'
    row.append(priority)
  elif opcion == '2':
    priority = 'Media'
    row.append(priority)
  else:
    priority = 'Baja'
    row.append(priority)
  todoList.append(row)
  clearScreen(1)
  print(f"Agregando {row[0]}...")
  clearScreen(1)
  print(f"{row[0]} agregada.")
  return todoList


def setLen(todoList):
  maxLen = 10
  for row in todoList:
    if len(row[0]) > maxLen:
      maxLen = len(row[0])
  return maxLen


def changeColor(priority):
  if priority == 'Alta':
    return "\033[0;31m"
  elif priority == 'Media':
    return "\033[1;33m"
  elif priority == 'Baja':
    return "\033[0;32m"


def printList(todoList, longestTask):
  clearScreen(0.5)
  if len(todoList) == 0:
    print(
      'No hay tareas añadidas, por favor añade una nueva tarea desde el menu inicial'
    )
    print()
    input('Para continuar presione la tecla ENTER')
  else:
    longitud_total = longestTask + 36
    longitud_igual = longitud_total
    print(f"|{'Tarea':^{longestTask+4}}|{'Fecha':^14}|{'Prioridad':^18}|")
    separateBar = f"{'=' * longitud_igual}"
    print(f"{separateBar:^{longestTask}}")
    for row in todoList:
      print(
        f"{changeColor(row[2])}|{row[0]:^{longestTask+4}}|{row[1]:^14}|{row[2]:^18}|"
      )
    print("\033[0m")
    opcion = input("Para salir presione la tecla ENTER ")
    if opcion:
      return


def editTask(todoList):
  clearScreen(0.5)
  print("Elige la tarea que quieras editar")
  for index, task in enumerate(todoList):
    print(f"{index + 1}. {task[0]}")
  index = int(input("> "))
  if index > len(todoList):
    print("Esta tarea no existe")
  else:
    clearScreen(1)
    print(f"Editando {todoList[index - 1][0]}")
    row = []
    task = input('¿Como se llamará ahora esta tarea?\n> ')
    row.append(task)
    dueDate = input(
      'Introduce la nueva fecha\nEl formaro es dd/mm/YYYY\n> ')
    row.append(dueDate)
    opcion = input(
      '¿Cual es la nueva prioridad?\nEscriba el numero de la opción\n1. Alta\n2. Media\n3. Baja\n> '
    )
    if opcion == '1':
      priority = 'Alta'
      row.append(priority)
    elif opcion == '2':
      priority = 'Media'
      row.append(priority)
    else:
      priority = 'Baja'
      row.append(priority)
    clearScreen(1)
    print("Guardando nueva tarea...")
    clearScreen(1)
    print("Nueva tarea guardada.")
    todoList[index - 1] = row


def deleteTask(todoList):
  clearScreen(1)
  print("Elige la tarea que quieras eliminar")
  for index, task in enumerate(todoList):
    print(f"{index + 1}. {task[0]}")
  index = int(input("> "))
  if index > len(todoList):
    print("Esta tarea no existe")
  else:
    taskToDelete = todoList[index - 1]
    clearScreen(1)
    print(f"¿Confirma que quiere eliminar {taskToDelete[0]} de la lista?\nLuego de esta accion no podrá recuperarse\ns/n")
    opcion = input("> ")
    if opcion == 's':
      clearScreen(1)
      print(f"Eliminando {taskToDelete[0]}")
      clearScreen(1)
      print("Tarea eliminada.")
      todoList.remove(taskToDelete)
      return todoList
    else: 
      return todoList

todoList = [['jugar', '04/19/2025', 'Alta']]

while True:
  clearScreen(1)
  print(f"🌟Life Organizer🌟")
  print('Bievenido al Organizador de vida, un gestor de tareas pendientes.')
  print('¿Que quieres hacer?')
  print(
    "1. Añadir\n2. Ver todas las tareas\n3. Editar una tarea\n4. Eliminar una tarea\n5. Salir"
  )
  opcion = input("> ")
  if opcion == '1':
    todoList = addTask(todoList)
  elif opcion == '2':
    longestTask = setLen(todoList)
    printList(todoList, longestTask)
  elif opcion == '3':
    editTask(todoList)
  elif opcion == '4':
    todoList = deleteTask(todoList)
  elif opcion == '5':
    clearScreen(1)
    print("Gracias por usar nuestra aplicación")
    clearScreen(2)
    exit()
  else:
    continue
