import random, time, os

def roll_dice(sides):
  result = random.randint(1, sides)
  return result


def create_health():
  six_sided_roll = roll_dice(6)
  twelve_sided_roll = roll_dice(12)
  result = ((six_sided_roll * twelve_sided_roll) / 2) + 10
  return round(result, 0)


def create_strength():
  six_sided_roll = roll_dice(6)
  twelve_sided_roll = roll_dice(12)
  result = ((six_sided_roll * twelve_sided_roll) / 2) + 12
  return round(result, 0)


def create_character():
  while True:
    time.sleep(1)
    character_name = input("Ponle un nombre: ")
    time.sleep(1)
    character_type = input("Elige el tipo del personaje (humano, elfo. vampiro, ogro...) ")
    time.sleep(1)
    vida = create_health()
    time.sleep(1)
    fuerza = create_strength()
    os.system('clear')
    print(f"""
      Nombre: {character_name}
      Tipo: {character_type}
      Vida: {vida}
      Fuerza: {fuerza}
    """)
    answer = input("¿Quieres crear un personaje nuevo? s/n > ")
    if answer == 's':
      continue
    else:
      os.system('clear')
      print('adios')
      exit()


print("Construyamos un caracter de video juegos")
create_character()
