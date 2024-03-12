def es_bisiesto(year):
  """
  Esta función determina si un year dado es bisiesto o no.
  """
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
      return True
  else:
      return False


year = int(input('Introduce el año: '))
if es_bisiesto(year):
  print(f"""
    El año {year} tiene:
      12 Meses
      366 dias
      {format(366*24, ',').replace(',', '.')} Horas
      {format(366*24*60, ',').replace(',', '.')} Minutos
      {format(366*24*60*60, ',').replace(',', '.')} Segundos
  """)
else:
  print(f"""
    El año {year} tiene:
      12 Meses
      365 dias
      {format(365*24, ',').replace(',', '.')} Horas
      {format(365*24*60, ',').replace(',', '.')} Minutos
      {format(365*24*60*60, ',').replace(',', '.')} Segundos
  """)