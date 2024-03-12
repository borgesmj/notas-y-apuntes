# Dia 4: Reto - Pongamos un poco de color
Todos aman las buenas historias
Bueno, vamos a crear una historia donde colocaremos al usuario como el personaje principal.

## Listas
Primero pediremos al usuario una gran cantidad de informacion sobre ellos, cosas que le gustan, cosas que odian, nombres de familiares y amigos

print("""
  Bienvenido a tu simulacion de aventura.
  Yo voy a hacerte unas preguntas y con esas voy a crear una historia increible contigo como la estrella.
""")
print()
my_name = input("Cual es tu nombre?: ")
print()
my_enemy = input("Cual es el nombre de tu peor enemigo?: ")
print()
my_superpower = input("Cual es tu superpoder?: ")
print()
my_live = input("Donde vives?: ")
print()
my_food = input("Cual es tu comida favorita?: ")

print(f"""
Hola {my_name}! Tu habilidad {my_superpower} asegurará que {my_enemy} no vuelva a verte a la cara nuevamente. Ve, y come {my_food} mientras caminas por las calles de {my_live} y usas {my_superpower} para bien y no para mal, 
""")

``````

Notese que colocamos una f antes de las triples comillas ("""), eso nos ayuda a concatenar variables y texto sin cerrar las comillas 