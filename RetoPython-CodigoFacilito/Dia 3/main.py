import re
from tabulate import tabulate

lista_usuarios = []
usuario_nuevo = {}
id = 0

# Creo que aqui iria bien OPP, pero no se me da muy bien
# El programa lo dividi en pequeñas funciones
# y nunca se detiene a menos que el usuario lo indique
# mantiene los datos guardados en una lista mientras el programa
# esté en ejecucion

#############################################################
# funcion para generar un ID
# mi objetivo era crear un ID aleatorio y unico
# pero no lo logré =)
def generateId():
  global id
  id += 1
  return id


#############################################################
# Esta funcion es para crear un usuario nuevo, de la clase pasada
def crear_usuario():
  # solicitar los nombres
  print()
  nombres = input("Ingrese los nombres del usuario > ")

  # Solicitar los apellidos
  print()
  apellidos = input('Ingrese los apellidos del usuario > ')

  #Solicitar el numero de telefono
  print()

  #utilizaremos regex para validar que el usuario ingrese un numero de telefono valido
  def validar_telefono(telefono):
    regex = r'^\d{10}$'
    # d => indica que hay uno o mas digitos numericos
    # {10} => indica que hay 10 digitos numericos
    return re.match(regex, telefono)

  # solicitamos el numero de telefono al usuario con una variable temporal
  # si el usuario introduce un numero de telefono valido, el programa continuara pidiendo
  # si el usuario coloca el correcto, lo guardará en la variable final
  temp_num_telefono = input("Ingrese el numero de telefono del usuario  > ")
  while (not validar_telefono(temp_num_telefono)):
    temp_num_telefono = input(
        'Por favor, ingrese un número de telefono válido > ')
  else:
    num_telefono = temp_num_telefono

  #Solicitar correo electronico
  print()

  #utilizaremos regex para validar que el usuario ingrese un correo electronico valido
  def validar_correo(correo):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-z]+\.com$'
    return re.match(regex, correo)

  temp_email = input('Ingrese el correo electronico del usuario > ')
  print()
  while (not validar_correo(temp_email)):
    temp_email = input('Por favor, ingrese un correo electronico válido > ')
  else:
    # solo pude evaluar que la longitud no fuese menor a 50
    # ya que @gmail.com o cualquier otro correo
    # es mayor a 5 caracteres
    if len(temp_email) > 50:
      temp_email = input(
          'Por favor, ingrese un correo electronico válido, menor a 50 caracteres > '
      )
    else:
      email = temp_email
  usuario_nuevo = {
      'id': generateId(),
      'Nombres': nombres,
      'Apellidos': apellidos,
      'Numero de telefono': num_telefono,
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


#############################################################
# esta funcion es para consultar usuarios registrados
# utilice tabulate
# busqué que era semejante en python a console.table() en JavaScript
def consultar_usuarios():
  print(tabulate(lista_usuarios, headers='keys'))
  menu_inicial()


################################################################
# Esta funcion es para el menu inicial, cada vez que el usuario termine
# de realizar un registro nuevo o consultar los hechos
# siempre va a volver al menu inicial
def menu_inicial():
  print()
  print("""
    Menu:
    1. Consultar usuarios registrados
    2. Registrar nuevo usuario
  """)
  while True:
    opcion = input("Ingrese la opción que quiere realizar: ")

    if opcion == "1":
      if len(lista_usuarios) == 0:
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
    else:
      print("Opción inválida")
      continue


# la pantalla prinicpal, solo aparece una vez, cuando el programa se ejecuta
print("""
  ###########################################
  #                                         #
  #     Bienvenido al registro de usuarios  #
  #                                         #
  ###########################################
""")

menu_inicial()
generateId()
