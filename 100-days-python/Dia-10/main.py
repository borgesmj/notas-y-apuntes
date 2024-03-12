myBill = float(input("¿Cuanto fue la cuenta?: "))
print()
serviceTip = 0
total_de_la_cuenta = 0
while True:
  if serviceTip < 1 or serviceTip > 20: 
    print('¿Cuanto es el porcentaje de propima que dejarán?')
    serviceTip = float(input('introducelo en numero, del 1 al 20: '))
    continue
  else:
    serviceTip = serviceTip/100
    serviceTip = serviceTip * myBill
    total_de_la_cuenta = serviceTip + myBill
    break
print(f"""
    La cuenta es: {myBill}
    La propina es: {round(serviceTip)}

    Total: {total_de_la_cuenta}
""")
print()
numero_de_personas = int(input('¿entre cuentas personas será dividida la cuenta?: '))
respuesta = total_de_la_cuenta/numero_de_personas
print()
print(f"Todos deben {round(respuesta,2)}")