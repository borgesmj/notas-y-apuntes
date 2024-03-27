import os, time
scores = []

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

print('Tabla de puntajes')
for row in scores:
  print(row)
time.sleep(2)
os.system('clear')
print('Calculando...')
time.sleep(2)
os.system('clear')
higscore = 0
name = None

for row in scores:
  data = row.split()
  if data:
    if int(data[1]) > higscore:
      higscore = int(data[1])
      name = data[0]

print(f"El puntaje ganador es de {name} con {higscore} puntos")