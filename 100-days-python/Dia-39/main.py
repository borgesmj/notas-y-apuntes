import random, os, time

lista_de_palabras = [
  "britanico", "suave", "integridad", "acento", "malvado", "genio"
]
palabra_elegida = random.choice(lista_de_palabras)
letras_usadas = []
vidas = 6
HANGMANPICS = [
  '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
                +---+
                |   |
                    |
                    |
                    |
                    |
              ========='''
]

while True:
  time.sleep(1)
  os.system('clear')
  all_letters = True
  for letter in palabra_elegida:
    if letter in letras_usadas:
      print(letter, end='')
    else:
      print('_', end='')
      all_letters = False
  print()

  if all_letters:
    print(f'ganaste con {vidas} restantes')
    break
  print()
  print(HANGMANPICS[vidas])
  print(f"tienes {vidas} vidas")
  nueva_letra = input("Introduce una letra > ").lower()
  if nueva_letra in letras_usadas:
    print('ya usaste esa letra antes')
    continue
  else:
    letras_usadas.append(nueva_letra)

  if nueva_letra not in palabra_elegida:
    print('Esa letra no está en la palabra')
    vidas -= 1
  else:
    print(f"{nueva_letra} si está en la palabra")

  if vidas <= 0:
    time.sleep(1)
    os.system('clear')
    print(HANGMANPICS[0])
    print("PERDISTE")
    print(f"La palabra era {palabra_elegida}")
    break
  else:
    continue
exit()
