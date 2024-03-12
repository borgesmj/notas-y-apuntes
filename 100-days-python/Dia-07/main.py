print("""
#################################
# ¿Eres un gran fan de Friends? #
#################################
""")
print()
print('Responde las preguntas para saberlo.')
print()
glasses = input('¿Alguien usa gafas? si o no >')
if glasses == 'si':
  print('No eres nada fan de Friends')
else:
  print('Puedes seguir')
  print()
  jenny = input('¿Cómo se llama la hermana de Ross? >')
  if jenny == 'Jenny':
    print('No eres nada fan de Friends')
  else:
    print('Puedes seguir')
    print()
    monica = input('¿Monica trabaja en un museo? si o no> ')
    if monica == 'si':
      print('No eres nada fan de Friends')
    else:
      print('Puedes continuar')
      print()
      amigo_ross = input('¿Quién es el mejor amigo de Ross? > ')
      if (amigo_ross == 'Joey') or (amigo_ross == 'joey'):
        print("""
        #############################################
        Las has respondido todas, eres fan de friends
        #############################################
        """)
      else:
        print('No eres nada fan de Friends')