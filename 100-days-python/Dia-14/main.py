# Two player 🪨📄✂️
from getpass import getpass as input

jugador_1_wins=0
jugador_2_wins=0

print("""
   Piedra, papel o Tijeras 🪨 📄 ✂️
   Ganando dos de tres
""")
print()
while (jugador_1_wins < 2) and (jugador_2_wins < 2):
  print("""
    Jugador 1, elige:
    Tienes que escribir el numero de tu seleccion
    1 => Piedra 🪨
    2 => Papel 📄
    3 => Tijeras ✂️
  """)
  jugador_1 = int(input('> '))
  print("""
  Jugador 2, elige:
  Tienes que escribir el numero de tu seleccion
  1 => Piedra 🪨
  2 => Papel 📄
  3 => Tijeras ✂️
""")
  jugador_2 = int(input('> '))
  if jugador_1 == jugador_2:
      print("Es un empate!!!")
  else:
    if jugador_1 == 1:
      if jugador_2 == 2:
        print("""
          Jugador 1: Piedra
          Jugador 2: Papel

          Jugador 2 Gana
        """)
        jugador_2_wins += 1
        print(f"""
          ganadas jugador 1 = {jugador_1_wins}
          ganadas jugador 2 = {jugador_2_wins} 
        """)
      else:
        print("""
          Jugador 1: Piedra
          JUgador 2: Tijeras

          Jugador 1 Gana
        """)
        jugador_1_wins += 1
        print(f"""
          ganadas jugador 1 = {jugador_1_wins}
          ganadas jugador 2 = {jugador_2_wins} 
        """)
    elif jugador_1 == 2:
      if jugador_2 == 1:
        print("""
          Jugador 1: Papel
          Jugador 2: Piedra

          Jugador 1 Gana
        """)
        jugador_1_wins += 1
        print(f"""
          ganadas jugador 1 = {jugador_1_wins}
          ganadas jugador 2 = {jugador_2_wins} 
        """)
      else:
        print("""
          Jugador 1: Papel
          Jugador 2: Tijeras

          Jugador 2 Gana
        """)
        jugador_2_wins += 1
        print(f"""
          ganadas jugador 1 = {jugador_1_wins}
          ganadas jugador 2 = {jugador_2_wins} 
        """)
    elif jugador_1 == 3:
      if jugador_2 == 1:
        print("""
          Jugador 1: Tijeras
          Jugador 2: Piedra

          Jugador 2 Gana
        """)
        jugador_2_wins += 1
        print(f"""
          ganadas jugador 1 = {jugador_1_wins}
          ganadas jugador 2 = {jugador_2_wins} 
        """)
      else:
        print("""
          Jugador 1: Tijeras
          Jugador 2: Papel

          Jugador 1 Gana
        """)
        jugador_1_wins += 1
        print(f"""
          ganadas jugador 1 = {jugador_1_wins}
          ganadas jugador 2 = {jugador_2_wins} 
        """)
else:
  if (jugador_1_wins == 2):
    print("jugador 1 ganador absoluto")
  else:
    print("jugador 2 ganador absoluto")