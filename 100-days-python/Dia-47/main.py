import time, os, random


def clearScreen(seconds):
  time.sleep(seconds)
  os.system('clear')


def mainGame(scorePlayer, scorePC):
  characters = {}
  characters['PORYGON'] = {
    'hp': 65,
    'ataque': 60,
    'defensa': 70,
    'ataque-especial': 85,
    'defensa-especial': 75,
    'velocidad': 40
  }
  characters['PIKACHU'] = {
    'hp': 35,
    'ataque': 55,
    'defensa': 40,
    'ataque-especial': 50,
    'defensa-especial': 50,
    'velocidad': 90
  }
  characters['BLASTOISE'] = {
    'hp': 79,
    'ataque': 83,
    'defensa': 100,
    'ataque-especial': 85,
    'defensa-especial': 105,
    'velocidad': 78
  }
  characters['CHARIZARD'] = {
    'hp': 78,
    'ataque': 84,
    'defensa': 78,
    'ataque-especial': 109,
    'defensa-especial': 85,
    'velocidad': 100
  }
  characters['DROWZEE'] = {
    'hp': 60,
    'ataque': 48,
    'defensa': 45,
    'ataque-especial': 43,
    'defensa-especial': 90,
    'velocidad': 42
  }
  characters['ALAKAZAM'] = {
    'hp': 55,
    'ataque': 50,
    'defensa': 45,
    'ataque-especial': 135,
    'defensa-especial': 95,
    'velocidad': 120
  }
  while scorePlayer < 5 and scorePC < 5:
    clearScreen(1)
    print(f"USUARIO: {scorePlayer}")
    print(f"PC: {scorePC}")
    print('Elige tu personaje')
    print()
    for index, (pokemon, _) in enumerate(characters.items(), 1):
      print(f"{index}. {pokemon}")
    time.sleep(1)
    opcion = input('> ')
    if int(opcion) > len(list(characters.keys())):
      print('ese pokemon no existe en nuestra lista')
    else:
      user = list(characters.keys())[int(opcion) - 1]
      print(f"Has elegido a {user}")
      comp = random.choice(list(characters.keys()))
      if user == comp:
        continue
      else:
        print("Elige la estadistica")
        estadisticas = [
          'hp', 'ataque', 'defensa', 'ataque-especial', 'defensa-especial',
          'velocidad'
        ]
        for index, estadistica in enumerate(estadisticas, 1):
          print(f"{index}. {(estadistica).upper()}")
        opcion = input("> ")
        estadistica = estadisticas[int(opcion) - 1]
        clearScreen(1)
        print(f"El usuario ha elegido {user}")
        print(f"El computador ha elegido {comp}")
        print(f"Se batallaran en {estadistica}")
        clearScreen(3)
        if characters[user][estadistica] > characters[comp][estadistica]:
          print(f'{user} ganador')
          scorePlayer += 1
        else:
          print(f'{comp} ganador')
          scorePC += 1
  else:
    if scorePlayer == 5:
      return 'Tu eres el ganador\nEres un gran maestro pokemon'
    else:
      return 'Has perdido contra la PC.\nNecesitas entrenas mucho mas'


def instrucciones():
  scorePlayer = 0
  scorePC = 0
  print(
    "Bienvenido a lucha pokemon\nEste juego consiste en una lucha en tiempo real... de estadisticas \U0001F601\n1. El uruario elige un pokemon de la lista\n2. La computadora elige el suyo\n3. Se elige una de las estadisticas de la carta a comparar\n4. Quien tenga el valor mas alto, gana la ronda\n5. Gana Quien tenga 5 victorias primero"
  )
  print()
  input('presione Enter para continuar...')
  winner = mainGame(scorePlayer, scorePC)
  clearScreen(2)
  print(winner)


instrucciones()