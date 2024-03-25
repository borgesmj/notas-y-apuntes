import random
pokebeast = {}

def prettyPrint(pokebeast):
  for key, value in pokebeast.items():
    print(key, end=': ')
    for subKey, subValue in value.items():
      print(subKey, subValue, end=' | ')

while True:
  types = ['wather', 'fire', 'earth', 'air', 'spirit']
  name = input('Input the beast name > ')
  element = random.choice(types)
  special_move = input("Input the special move > ")
  HP = int(input("Input the beast starting HP > "))  
  MP = int(input("Input the beast starting MP > "))
  pokebeast[name] = {
    'element': element,
    'special_move': special_move,
    'HP': HP,
    'MP': MP
  }
  option = input("again? s/n > ")
  if option == 's':
    continue
  else:
    break

prettyPrint(pokebeast)