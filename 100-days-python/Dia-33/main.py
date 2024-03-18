import time, os

my_list = []


def print_list():
  print()
  if len(my_list) == 0:
    os.system("clear")
    print(
      "\033[0;31m", """
    ##################################
    Aun no hay ningun item en la lista
    ##################################
    """)
    opcion = input("Presione enter para continuar: ")
    if opcion == "":
      os.system("clear")
      menu_incial()
  else:
    os.system("clear")
    for item in my_list:
      print("\033[0;32m", f"✅ {item}\n")
    print()
    opcion = input("Presione enter para continuar ")
    if opcion == "":
      os.system("clear")
      menu_incial()


def add_item():
  os.system("clear")
  print("\033[0;36m", "Introduce la tarea que se va a realizar: ")
  tarea = input("> ")
  my_list.append(tarea)
  print(f"agregando {tarea}")
  time.sleep(1)
  os.system("clear")
  print(f"{tarea} agregada")
  time.sleep(2)
  os.system("clear")
  menu_incial()


def delete_item():
  os.system("clear")
  if len(my_list) == 0:
    os.system("clear")
    print(
      "\033[0;31m", """
    ##################################
    Aun no hay ningun item en la lista
    ##################################
    """)
    opcion = input("Presione enter para continuar: ")
    if opcion == "":
      os.system("clear")
      menu_incial()
  else:
    os.system("clear")
    index = 0
    for item in my_list:
      print(f"{index + 1}.- {item}")
      index += 1
    print("Escriba el numero de la tarea a eliminar")
    opcion = int(input("> "))
    if opcion > len(my_list):
      print("opcion no valida")
      time.sleep(1)
      os.system("clear")
      menu_incial()
    else:
      print(f"¿Eliminar {my_list[opcion - 1]} de la lista?")
      opcion = input("s/n > ")
      if opcion.lower() == "s":
        print("eliminando...")
        time.sleep(1)
        opcion_eliminar = my_list[0]
        my_list.remove(opcion_eliminar)
        time.sleep(1)
        print("Eliminado exitosamente")
        time.sleep(1)
        os.system("clear")
      elif opcion.lower() == "n":
        os.system("clear")
        menu_incial()
      else:
        print(
          "\033[0;31m", """
        ##################################
        Opcion no válida
        ##################################
        """)
        time.sleep(1)
        os.system("clear")


def menu_incial():
  while True:
    print("\033[0;34m", "Administrador de quehaceres")
    print("\033[0;34m", "Selecciona una opcion del menu")
    print("""
        1. Añadir
        2. Ver la lista
        3. Eliminar tarea realizada
    """)
    menu = input("> ")
    if int(menu) == 1:
      add_item()
    elif int(menu) == 2:
      print_list()
    elif int(menu) == 3:
      delete_item()
    else:
      print(
        "\033[0;31m", """
      ##################################
      Opcion no válida
      ##################################
      """)
      time.sleep(1)
      os.system("clear")


menu_incial()