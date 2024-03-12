import random 

def rollDice(sides):
  while True:
    myNumber = random.randint(1,sides)
    print("Sacaste ",myNumber)
    answer= input("Quieres continuar? s/n: ")
    if answer == 's':
      continue
    else:
      print("adios")
      break


sides = int(input("¿Cuantos lados quieres que tenga el dado?: "))
rollDice(sides)
