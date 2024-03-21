import random
print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")

new_mokebeast = {
  'name': None,
  'type': None,
  'especial-move': None,
  'HP': None,
  'MP': None
}

def change_color(type):
  if type == 'fire':
    print("\033[0;31m")
  elif type == 'water':
    print("\033[0;34m")
  elif type == 'earth':
    print("\033[0;33m")
  elif  type == 'air':
    print("\033[0;32m")
  else:
    print("\033[1;33m")


types = ['wather', 'fire', 'earth', 'air', 'spirit']
for name in new_mokebeast.keys():
  print("\033[0m")
  if name == 'type':
    new_mokebeast[name]= random.choice(types)
  else:
    new_mokebeast[name]= input(f"Introduce your beast's {name}> ")

change_color(new_mokebeast['type'])

for name, value in new_mokebeast.items():
  print(f"{name : >15}: {value : <17}")