import random

print("""
    Bienvenido usuario al juego de adivina el número.
    1. Vas a adivinar un numero entre 1 y... 1.000.000
    2. No hay limite de intentos
    3. Si colocas un numero muy bajo te diremos que la respuesta es mas alta, y si colocs uno muy alto, te diremos que bajes.
  """)
print()
attemps = 0
correct_number = random.randint(1, 1000000)
print(correct_number)
while True:
    print()
    print("Adivina el numero")
    attemp_number = int(input(' > '))
    if attemp_number <= 0:
        print("Debes colocar un numero valido")
        exit()
    else:
        if attemp_number < correct_number:
            print(f"{attemp_number} es muy bajo, súbele mas")
            attemps += 1
        elif attemp_number > correct_number:
            print(f"{attemp_number} es muy alto, bájale")
            attemps += 1
        else:
            print("correcto!!! Adivinaste el numero  🥳🥳")
            attemps += 1
            print(f"Lo adivinaste en {attemps} intentos")
            exit()
