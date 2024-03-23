import random, os, time


def random_number():
  number = random.randint(1, 90)
  return number


numbers = []
for i in range(8):
  number = random_number()
  if number not in numbers:
    numbers.append(number)
numbers.sort()

bingo = [[numbers[0], numbers[1], numbers[2]],
         [numbers[3], 'BINGO!', numbers[4]],
         [numbers[5], numbers[6], numbers[7]]]


def prettyPrint(bingo):
  time.sleep(1)
  os.system("clear")
  print("\033[1;33m")
  print(f'{"BINGO":^30}')
  print(f'{"_________________________":<30}')
  for row in bingo:
    for cell in row:
      print(f"| {cell:^6}|", end='')
    print()


def evalNumber(bingo, number):
  for i, row in enumerate(bingo):
    if number in row:
      index = row.index(number)
      return (i, index)


def evalCard(bingo):
  fullCard = [
    ['x', 'x', 'x'],
    ['x', 'BINGO!', 'x'],
    ['x', 'x', 'x'],
  ]
  if bingo == fullCard:
    return True


def playBingo(bingo):
  while True:
    win = evalCard(bingo)
    if win:
      prettyPrint(bingo)
      print('HA GANADO!!')
      break
    else:
      prettyPrint(bingo)
      number = int(input("¿Que numero salio?: "))
      index = evalNumber(bingo, number)
      if index:
        x = index[0]
        y = index[1]
        bingo[x][y] = 'x'
      else:
        continue


playBingo(bingo)
