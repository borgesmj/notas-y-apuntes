print("Generemos una lista")
print()
print("Ingresa el numero de inicio")
initial = int(input("> "))
print("Ingresa el numero final")
final = int(input("> "))
print("Ingresa la cantidad del incremento")
increase = int(input("> "))
if (initial > final):
  increase = increase * -1
print()
if increase > 0:
  print(f"""
  Comienza en: {initial}
  Termina en: {final}
  Aumento de: {increase} en {increase}
  """)
else:
  print(f"""
  Comienza en: {initial}
  Termina en: {final}
  Disminucion de: {increase} en {increase}
  """)
for i in range(initial, final, increase):
    print(i)
