print("🌟Generador de nombres de Star Wars🌟")
print()
first_name = input("Introduce tu primer nombre:\n>")
first_name = first_name.strip().lower()[0:3]
print()
last_name = input("Introduce tu apellido:\n>")
last_name = last_name.strip().lower()[0:3]
print()
mother_maiden_name = input("Ahora intrduce el apellido de soltera de tu mama:\n>")
print()
mother_maiden_name = mother_maiden_name.strip().lower()[0:2]
born_city = input("Introduce la ciudad donde naciste:\n>")
born_city = born_city.strip().lower()[0:3]
born_city = born_city[::-1]
print()
sw_first_name = (f"{first_name}{last_name}").title()
sw_last_name = (f"{mother_maiden_name}{born_city}").title()
print()
print(f"Tu nombre de Star Wars es {sw_first_name} {sw_last_name}")