import os, time, platform

my_list = ["tatata"]


def clean_screen():
  time.sleep(1)
  if platform.system() == 'Windows':
    os.system("cls")  # Comando para limpiar pantalla en Windows
  else:
    os.system("clear")


def check_list(task):
  if task in my_list:
    return True
  else:
    return False


def add_new():
  clean_screen()
  print("Introduce la tarea a realizar")
  new_task = input("> ")
  check_task = check_list(new_task)
  if check_task:
    clean_screen()
    print("Ya esa tarea está inluida en la lista")
    clean_screen()
  else:
    clean_screen()
    print(f"Agregando {new_task}")
    clean_screen()
    print(f"{new_task} agregada")
    my_list.append(new_task)
    print_menu()


def print_list():
  clean_screen()
  if len(my_list) == 0:
    print(
      "\033[0;31m", """
    ###########################
    La lista aun no contiene 
    tareas, por favor introduce 
    una desde el menu de inicio
    ###########################
    """)
    print("\u001b[0m")
    print("Presione enter para continuar")
    option = input("> ")
    if option == "":
      print_menu()
  else:
    print("Lista de tareas:")
    for i in range(0, len(my_list)):
      print(f"{i + 1}. {my_list[i]}")
    print()
    print(
      "Si desea editar un item de la lista, escriba el numero. de lo contrario, presione enter"
    )
    option = input("> ")
    if option == "":
      print_menu()
    elif (int(option)) > (len(my_list)):
      print("Ese item no existe")
      print_list()
    else:
      modified_task = input("Escriba la nueva tarea: ")
      check_task = check_list(modified_task)
      if check_task:
        clean_screen()
        print("NO puede ser modificada. Ya esa tarea está inluida en la lista")
        clean_screen()
      else:
        my_list[int(option) - 1] = modified_task
        clean_screen()
        print("Modificando tarea")
        clean_screen()
        print("Agregando nueva tarea")
        clean_screen()
        print("Tarea modificada")
        print_menu()


def delete_task():
  clean_screen()
  if len(my_list) == 0:
    print(
      "\033[0;31m", """
    ###########################
    La lista aun no contiene 
    tareas, por favor introduce 
    una desde el menu de inicio
    ###########################
    """)
    print("\u001b[0m")
    print("Presione enter para continuar")
    option = input("> ")
    if option == "":
      print_menu()
  else:
    print("Lista de tareas:")
    for i in range(0, len(my_list)):
      print(f"{i + 1}. {my_list[i]}")
    print()
    print(
      "Escoja el número de la tarea a borrar, de lo contrario presione enter para ir al menu inicial"
    )
    option = input("> ")
    if option == "":
      print_menu()
    elif (int(option)) > (len(my_list)):
      print("Ese item no existe")
      print_list()
    else:
      delete_option = my_list[int(option) - 1]
      print(f"¿Desear borrar {delete_option}? s/n")
      option = input("> ")
      if option == "s":
        clean_screen()
        print(f"Borrando {delete_option}")
        my_list.remove(delete_option)
        clean_screen()
        print(f"{delete_option} borrado")
        print_menu()
      else:
        print_menu()


def progress_bar(steps, tasks):
  while my_list:
    task_to_delete = my_list[0]
    my_list.remove(task_to_delete)
  for i in range(steps):
    print("[*]", end="", flush=True)
    time.sleep(0.5)


def delete_all():
  if len(my_list) == 0:
    clean_screen()
    print("NO HAY ELEMENTOS EN SU LISTA")
  else:
    clean_screen()
    print("¿ESTAS SEGURO DE QUERER BORRAR TODA LA LISTA?")
    print("Si lo haces no hay manera de recuperarlo")
    print("s/n")
    option = input("> ")
    if option == "s":
      clean_screen()
      progress_bar(10, my_list)
      clean_screen()
      print("Borrado con exito")
    else:
      print_menu()


def print_menu():
  while True:
    clean_screen()
    print(
      "\u001b[32m", """
    ###########################
        Bienvenido usuario al 
        Gestor de pendientes
    ###########################
    """)
    print()
    print(
      "Selecciona una opcion:\n1. Añadir una nueva tarea\n2. Ver Lista de tareas\n3. Borrar una tarea\n4. Borrar todo"
    )
    opcion = input("> ")
    if opcion == "1":
      print("\u001b[0m")
      add_new()
    elif opcion == "2":
      print("\u001b[0m")
      print_list()
    elif opcion == "3":
      print("\u001b[0m")
      delete_task()
    elif opcion == "4":
      print("\u001b[0m")
      delete_all()
    else:
      continue


print_menu()
