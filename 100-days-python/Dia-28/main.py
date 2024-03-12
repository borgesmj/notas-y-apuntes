import random, time, os

characters = [
  #   {
  #   "nombre": "Samy",
  #   "tipo": "humana",
  #   "vida": 18,
  #   "fuerza": 21
  # }, {
  #   "nombre": "MIguek",
  #   "tipo": "ogro",
  #   "vida": 30,
  #   "fuerza": 36
  # }
]

messages = [
  'le da un golpe a',
  'le lanza un hechizo a',
  'patea a',
  'le lanza una pocion magica a'
]


def presentation(characters):
  print(f"""
  ######################################
      TENEMOS UNA NUEVA BATALLA!!!
  ######################################
  En la esquina azul tenemos a:
    {characters[0]['nombre']}
    Estadisticas:
      Tipo: {characters[0]['tipo']}
      Vida: {characters[0]['vida']}
      Fuerza: {characters[0]['fuerza']}

  Y en la esquina roja está:
    {characters[1]['nombre']}
    Estadisticas:
      Tipo: {characters[1]['tipo']}
      Vida: {characters[1]['vida']}
      Fuerza: {characters[1]['fuerza']}
  """)


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


def create_character(counter):
  os.system('clear')
  character_name = input(f"Ponle un nombre al personaje {counter}: ")
  character_type = input(
    "Elige el tipo del personaje (humano, elfo. vampiro, ogro...) ")
  print()
  print("creando tu personaje...")
  time.sleep(1)
  vida = create_health()
  fuerza = create_strength()
  return {
    "nombre": character_name,
    "tipo": character_type,
    "vida": vida,
    "fuerza": fuerza
  }

def battle(characters, ronda, message):
  # pick a winner
  turn_one = roll_dice(6)
  turn_two = roll_dice(6)
  if turn_one == turn_two:
    battle(characters, ronda, message)
  elif turn_one > turn_two:
    difference = characters[0]['fuerza'] - characters[1]['fuerza']
    damage = max(0, difference)
    characters[1]['vida'] -= damage
    print(f"""
      ###############################################
      {characters[0]['nombre']} {message} {characters[1]['nombre']}
      {characters[0]['nombre']} gana la ronda {ronda}
      a {characters[1]['nombre']} le queda {characters[1]['vida']} de vida
      ###############################################
      """)
  else:
    difference = characters[1]['fuerza'] - characters[0]['fuerza']
    damage = max(0, difference)
    characters[0]['vida'] -= damage
    print(f"""
      ###############################################
      {characters[1]['nombre']} {message} {characters[0]['nombre']}
      {characters[1]['nombre']} gana la ronda {ronda}
      a {characters[0]['nombre']} le queda {characters[0]['vida']} de vida
      ###############################################
      """)

def salir():
  exit()


def epic_battle():
  while True:
    while len(characters) < 2:
      time.sleep(1)
      os.system('clear')
      counter = len(characters) + 1
      new_character = create_character(counter)
      characters.append(new_character)
    else:
      time.sleep(1)
      os.system('clear')
      presentation(characters)
      siguiente = input("presione enter para continuar...")
      if siguiente == '':
        ronda = 1
        while (characters[0]['vida'] > 0) and (characters[1]['vida'] > 0):
          time.sleep(3)
          os.system('clear')
          index = random.randint(0, len(messages) - 1)
          message = messages[index]
          battle(characters, ronda, message)
          ronda += 1
        else:
          os.system('clear')
          if characters[0]['vida'] > 0:
            print(f"""
            ###########################################
            {characters[0]['nombre']} es el ganador!!!!
            ###########################################
            """)
            salir()
          else:
            print(f"""
            ###########################################
            {characters[1]['nombre']} es el ganador!!!!
            ###########################################
            """)
            salir()

epic_battle()
