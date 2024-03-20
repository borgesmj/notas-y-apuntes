# my_string = input("introduce una frase larga > ")
def change_color(letter):
  if letter == 'r':
    print("\033[0;31m", end='')
  elif letter == " ":
    print("\033[0m", end='')
  elif letter == 'b':
    print("\033[0;34m", end='')
  elif letter == 'g':
    print("\033[0;32m", end='')
  elif letter == 'p':
    print("\033[35m", end='')
  elif letter == 'y':
    print("\033[1;33m", end='')


my_string = 'En la primavera, los pájaros gorjean mientras las flores brotan en un brillante espectáculo de colores. El rojo de las rosas compite con el verde intenso del césped, mientras que el azul del cielo se refleja en el agua del río. Las mariposas revolotean entre las ramas, llevando consigo la promesa de días cálidos y soleados. Es un tiempo para relajarse y disfrutar de la belleza de la naturaleza, para contemplar la gran diversidad de tonalidades que nos rodean y nos recuerdan la riqueza de la vida.'


for letter in my_string:
    change_color(letter.lower())
    print(letter, end='')
print()

