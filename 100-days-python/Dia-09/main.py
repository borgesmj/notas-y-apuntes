print("""
  #####################################
  #    Generador de generaciones      #
  #####################################
""")
print()
year = int(input('¿Cual es tu año de nacimiento? sin puntos ni coma> '))
print()
if year >= 1925 and year <= 1946:
  print('Eres de la generacioin Tradicionalista')
elif year >= 1947 and year <= 1964:
  print('Eres de la generacion Baby Boomers')
elif year >=1965 and year <= 1981:
  print('Eres de la generacion X')
elif year >= 1982 and year <= 1995:
  print('Eres de los Millenials')
elif year >= 1996 and year <= 2015:
  print('Eres generacion z')
else:
  if year < 1925:
    print('¿Como sigues vivo?')
  elif year >= 2015 and year <= 2024:
    print('Eres un bebe')
  else:
    print('Ese año ni existe o no ha llegado')
print()
