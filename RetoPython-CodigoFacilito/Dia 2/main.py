import re  # Import the regex module

print("""
  ###########################################
  #                                         #
  #     Bienvenido al registro de usuarios  #
  #                                         #
  ###########################################
""")
users = int(input('¿Cuantos usuarios desea registrar? '))
counter = 0

while counter < users:
  # solicitar los nombres
  print()
  print(f"USUARIO NUMERO {counter+1}")
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
      temp_email = input('Por favor, ingrese un correo electronico válido, menor a 50 caracteres > ')
    else:
      email = temp_email
  print("""
  ###########################################
  #      Usuario registrado con exito       #
  ###########################################
  """)
  counter += 1
print(
    'Gracias por ver mi código, ¿y si me agregas al Github? Me encuentras como borgesmj =)'
)
