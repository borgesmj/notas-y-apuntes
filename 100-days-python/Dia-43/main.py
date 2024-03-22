import random

def random_number():
  number = random.randint(1,90)
  return number

numbers = []
for i in range(8):
  numbers.append(random_number())
numbers.sort()

bingo = [
  [numbers[0],numbers[1], numbers[2]],
  [numbers[3], 'BINGO!', numbers[4]],
  [numbers[5], numbers[6], numbers[7]]
]

def prettyPrint(bingo):
  print("\033[1;33m")
  print(f'{"BINGO":^30}')
  print(f'{"_________________________":^30}')
  for row in bingo:
      for cell in row:
          print(f"| {cell:^6}|", end='')
      print()

prettyPrint(bingo)