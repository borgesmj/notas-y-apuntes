attemps = 0
print("""
  Llena el espacio en blanco con el pedazo de letra que falta.
""")
while True:
    print('Never going to _________ you up.')
    lyric = input('> ').lower()
    if lyric == "give":
        attemps += 1
        break
    else:
        attemps += 1
print(f'Bien hecho!! y lo hiciste en {attemps} intentos')