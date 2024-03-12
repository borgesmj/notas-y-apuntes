initial_ammount = 1000
APR = 0.05
for years in range(10):
    initial_ammount += initial_ammount * APR
    print(f"Año {years+1}: prestamo es {round(initial_ammount, 2)}")