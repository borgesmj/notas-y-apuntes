import sys
import re
lista_usuarios = [
  {
    "nombres": "Miguel José",
    "apellidos": "Borges Medina",
    "telefono": "1234567890",
    "email": "correo@correo.com"
  },
  {
    "nombres": "Pedro Luis",
    "apellidos": "Perez Linares",
    "telefono": "9876543210",
    "email": "correo@correo.com"
  }
]

# lista_usuarios = []
usuario_nuevo = {}

def eliminar_usuario():
  print()
  print('Escriba el id del usuario a modificar')
  id_usuario = input('Si no desea eliminar ningun usuario, escriba el numero cero (0) > ')
  if id_usuario == '0':
    menu_consulta()
  elif int(id_usuario) <= len(lista_usuarios):
    print(f"¿Está seguro que quiere eliminar a {lista_usuarios[int(id_usuario) - 1]['nombres']}")
    confirmacion = input('s/n > ').lower()
    if confirmacion == 's':
      lista_usuarios.pop(int(id_usuario) - 1)
      print()
      print("""
          ¡¡¡
              Usuario Eliminado
                                !!!
      """)
      if len(lista_usuarios) == 0:
        menu_inicial()
      else:
        consultar_usuarios()
    elif confirmacion == 'n':
      consultar_usuarios()
    else:
      print()
      print('Respuesta invalida')
      menu_inicial()
  else:
    print("""
        ¡¡¡
            Ese usuario no existe
                              !!!
    """)
    print()
    menu_consulta()

def modificar_usuario(lista_usuarios):
  print()
  print('Escriba el id del usuario a modificar')
  id_usuario = input('Si no desea modificar ningun usuario, escriba el numero cero (0) > ')
  if id_usuario == "0":
    menu_consulta()
  elif int(id_usuario) <= len(lista_usuarios):
    usuario_modificar = lista_usuarios[int(id_usuario) - 1]
    print()
    nombres = input("Ingrese los nombres del usuario a modificar > ")
    usuario_modificar['nombres'] = nombres
    print()
    apellidos = input('Ingrese los apellidos del usuario > ')
    usuario_modificar['apellidos'] = apellidos
    lista_usuarios[int(id_usuario) - 1] = usuario_modificar
    def validar_telefono(telefono):
      regex = r'^\d{10}$'

      return re.match(regex, telefono)
    print()
    temp_num_telefono = input("Ingrese el numero de telefono del usuario  > ")
    while (not validar_telefono(temp_num_telefono)):
      temp_num_telefono = input(
          'Por favor, ingrese un número de telefono válido > ')
    else:
      num_telefono = temp_num_telefono
      usuario_modificar['telefono'] = num_telefono
    print()

    def validar_correo(correo):
      regex = r'^[a-zA-Z0-9_.+-]+@[a-z]+\.com$'
      return re.match(regex, correo)

    temp_email = input('Ingrese el correo electronico del usuario > ')
    print()
    while (not validar_correo(temp_email)):
      temp_email = input('Por favor, ingrese un correo electronico válido > ')
    else:
      if len(temp_email) > 50:
        temp_email = input(
            'Por favor, ingrese un correo electronico válido, menor a 50 caracteres > '
        )
      else:
        email = temp_email
        usuario_modificar['email'] = email
    print()
    print("""
        #####
            Usuario Modificado
                              ####
    """)
    print()
    consultar_usuarios()
  else:
    print("""
        ¡¡¡
            Ese usuario no existe
                              !!!
    """)
    print()
    menu_consulta()

def menu_consulta():
  print()
  print("""
    ¿Que desea hacer?
    1. Modificar un usuario registrado
    2. Eliminar usuario regisrado
    3. Agregar un usuario nuevo
    4. Salir al menu principal
  """)
  print()
  opcion =  input("Escriba el numero de la opcion de su preferencia > ")
  if opcion == "1":
    modificar_usuario(lista_usuarios)
  elif opcion == "2":
    eliminar_usuario()
  elif opcion == "3":
    crear_usuario()
  elif opcion == "4":
    menu_inicial()
  else:
    print("""
        ¡¡¡
            Opcion no válida
                              !!!
    """)
    menu_consulta()

def salir_programa():
  print()
  confirmar_salir = input("¿Está seguro? s/n > ").lower()
  if confirmar_salir == "s":
    print()
    print('Adios =)')
    sys.exit()
  else:
    menu_inicial()

def consultar_usuarios():
  print()
  print()
  print(f'|{"id".ljust(4)}|{"Nombres".ljust(22)}|{"Apellidos".ljust(21)}|{"Numero de telefono".ljust(21)}|{"email".ljust(21)}|')
  print("|----|----------------------|---------------------|---------------------|---------------------|")
  for  index, user in enumerate(lista_usuarios):
    print(f"|{str(index + 1).ljust(4)}|{user['nombres'].ljust(21)} |{user['apellidos'].ljust(20)} |{user['telefono'].ljust(20)} |{user['email'].ljust(20)} |")
  print("|----|----------------------|---------------------|---------------------|---------------------|")
  menu_consulta()

def crear_usuario():

  print()
  nombres = input("Ingrese los nombres del usuario > ")


  print()
  apellidos = input('Ingrese los apellidos del usuario > ')


  print()


  def validar_telefono(telefono):
    regex = r'^\d{10}$'

    return re.match(regex, telefono)


  temp_num_telefono = input("Ingrese el numero de telefono del usuario  > ")
  while (not validar_telefono(temp_num_telefono)):
    temp_num_telefono = input(
        'Por favor, ingrese un número de telefono válido > ')
  else:
    num_telefono = temp_num_telefono


  print()


  def validar_correo(correo):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-z]+\.com$'
    return re.match(regex, correo)

  temp_email = input('Ingrese el correo electronico del usuario > ')
  print()
  while (not validar_correo(temp_email)):
    temp_email = input('Por favor, ingrese un correo electronico válido > ')
  else:

    if len(temp_email) > 50:
      temp_email = input(
          'Por favor, ingrese un correo electronico válido, menor a 50 caracteres > '
      )
    else:
      email = temp_email
  usuario_nuevo = {
      'nombres': nombres,
      'apellidos': apellidos,
      'telefono': num_telefono,
      'email': email
  }
  lista_usuarios.append(usuario_nuevo)
  print()
  print("""
  ###########################################
  #      Usuario registrado con exito       #
  ###########################################
  """)
  menu_inicial()
    
def menu_inicial():
  print()
  print("""
    Menu:
    1. Consultar usuarios registrados
    2. Registrar nuevo usuario
    3. Salir
  """)
  while True:
    opcion = input("Ingrese la opción que quiere realizar: ")

    if opcion == "1":
      if len(lista_usuarios) == 0:
        print()
        print('Aun no hay usuarios registrados')
        opcion = input('Deseas registrar un usuario nuevo? (s/n): ').lower()
        if opcion == 's':
          crear_usuario()
        else:
          menu_inicial()
      else:
        consultar_usuarios()
      break
    elif opcion == "2":
      crear_usuario()
      break
    elif opcion == "3":
      salir_programa()
      break
    else:
      print("Opción inválida")
      continue

def saludo_inicial():
  print("""
    ###########################################
    #                                         #
    #     Bienvenido al registro de usuarios  #
    #                                         #
    ###########################################
  """)
  print()
  menu_inicial()



saludo_inicial()