import os, time
my_list = {
  "nombre": None,
  "url": None,
  "descripcion": None,
  "calificacion": None
}

for name in my_list.keys():
  print()
  if name == "calificacion":
    print("La calificacion tiene que ser de 1 a 5 *")
  my_list[name] = input(f"Introduzca el {name} del sitio web: ")

time.sleep(1)
os.system("clear")

for name, value in my_list.items():
  print(f"{name}: {value}")
