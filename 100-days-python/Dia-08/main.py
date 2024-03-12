print("""
  ##############################################
  #                                            #
  # Generador de insultos y chistes diarios    #
  #                                            #
  ##############################################
""")

name = input('¿Cual es tu nombre? > ').lower()
day_of_week = input('¿Cual es el dia de la semana? > ').lower()

if day_of_week == 'lunes':
  print(f"{name} eres tan brillante como una bombilla fundida")
elif day_of_week == 'martes':
  print(f'Si el talento se midiera en burbujas, tú serías una lata de refresco agitada, {name}.')
elif day_of_week == 'miercoles':
  print(f'Tu belleza es contagiosa, como un resfriado, {name}.')
if day_of_week == 'jueves':
  print(f'Si el talento se midiera en burbujas, tú serías una lata de refresco agitada, {name}.')
if day_of_week == 'virnes':
  print(f'Dime, {name}, ¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas.')
if day_of_week == 'sabado':
  print(f'¿Qué le dice una iguana a su hermana gemela, {name}? ¡Iguanita.!')
if day_of_week == 'domingo':
  print(f'Si la ignorancia fuera una moneda, tú serías millonario {name}')
else:
  print(f"Eres como un GPS sin señal, {name}, siempre perdido. {day_of_week} no existe")