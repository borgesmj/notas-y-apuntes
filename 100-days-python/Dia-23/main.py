def login():
  while True:
    username = input("¿Cual es tu nombre de usuario?: > ")
    password = input("¿Cual es tu contraseña? > ")
    if username == "David" and password == "Replit4ev#r":
      print("Bienvenido David!")
      break
    else:
      print("Ese no es el usuario y/o contraseña correcta")
      continue

print("LOGIN")
login()