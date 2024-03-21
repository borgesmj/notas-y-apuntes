libreta_de_contacto = {}
print("🌟Tarjeta de contacto🌟")
print()
nombre = input("Introduce tu nombre completo:\n>  ").strip().title()
print()
fecha_de_nacimiento = input(
  "Introduce tu fecha de nacimiento:\n>").strip().capitalize()
print()
telefono = str(input("Introduce tu numero de telefono:\n> ")).strip()
print()
email = input("Introduce tu correo electronico:\n>  ").strip()
print()
direccion = input("introduzca su direccion:\n> ").strip().title()
print()
libreta_de_contacto = {
  'nombre': nombre,
  'fecha_nacimiento': fecha_de_nacimiento,
  'telefono': telefono,
  'email': email,
  'direccion': direccion
}

print(
  f"Hola {libreta_de_contacto['nombre']}. Nuestro diccionario dice que naciste el {libreta_de_contacto['fecha_nacimiento']}, podemos llamarte al {libreta_de_contacto['telefono']}, enviarte un email a {libreta_de_contacto['email']}, o escribir a {libreta_de_contacto['direccion']}."
)
