import random


def rollDice(sides):
  result = random.randint(1, sides)
  return result


def createHealth():
  dice_one = rollDice(6)
  dice_two = rollDice(8)
  health = dice_one * dice_two
  return health


def createCaracter():
  while True:
    name = input("Nombra tu personaje: ")
    health = str(createHealth())
    print(f"Tu personaje se llama {name} y tiene una fuerza de {health} hp")
    print()
    repeat = input("¿Quieres crear otro? s/n > ")
    if repeat == 's':
      continue
    else:
      print('adios')
      exit()
      break


print("Creador de personajes")
createCaracter()
