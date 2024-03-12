print("""
  ###############################
  #                             #
  # LOGIN SYSTEM                #
  #                             #
  ###############################
""")
print()
username = input('Ingresa tu username > ')
password = input('Ingresa tu contraseña > ')
print()
if username == 'jose' and password == 'jose':
  print('Bienvenido Jose')
elif username == 'juan' and password == 'juan':
  print('Bienvenido Juan')
elif username == 'maria' and password == 'maria':
  print('Bienvenido Maria')
else:
  print('Usuario no encontrado y/o contraseña incorrecta')