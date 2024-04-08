import datetime

today = datetime.date.today() # Today's date
print('🌟Temporizador de cuenta atrás del evento🌟')
print()
evento = input('¿Cual es el evento? > ')
print("¿Cuando es el evento?")
year = int(input('Año > '))
month = int(input('Mes > '))
day = int(input('Dia > '))

eventDay = datetime.date(year, month, day)

if eventDay > today:
  difference = eventDay - today 
  print(f"Aun faltan {difference.days} dias para {evento}")
elif eventDay == today:
  print('🎉🎉 El evento es hoy!!! 🎉🎉')
else:
  print('el evento ya paso')

