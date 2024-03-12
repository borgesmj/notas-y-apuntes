print("""
  Bienvenido al sistema de calificacion
""")
print()
print("Primero vas a decirnos cuanto es el puntaje maximo de esta prueba")
puntaje_maximo = int(input("> "))
print("Ahora nos diras el puntaje que obtuviste")
puntaje_alumno = int(input("> "))
if puntaje_alumno > puntaje_maximo:
  print("Revisa bien, no puedes obtener mas puntos de los posibles")
else:
  porcentaje_calificacion = round((puntaje_alumno/puntaje_maximo), 2)
  porcentaje_calificacion = porcentaje_calificacion * 100
  print(porcentaje_calificacion)
  if porcentaje_calificacion >= 90:
    print("Excelente, obtuviste una A+, sigue asi!!!")
  elif porcentaje_calificacion >=80 and porcentaje_calificacion < 90:
    print("Genial! Obtiviste una A. Continua asi")
  elif porcentaje_calificacion >=70 and porcentaje_calificacion < 80:
    print("Muy bien! Obtiviste una B. Vas muy bien")
  elif porcentaje_calificacion >=60 and porcentaje_calificacion < 70:
    print("Obtuviste una C, se puede mejorar")
  elif porcentaje_calificacion >=50 and porcentaje_calificacion < 60:
    print("Obtiviste una D. Sigue intentando")
  else:
    print("Reprobaste, obtuviste una F")