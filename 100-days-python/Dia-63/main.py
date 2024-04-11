import subroutines as sr
import time


print('Aqui se imprimira un texto')
time.sleep(1)
sr.turnRed("Este texto se imprimirá en rojo")
time.sleep(1)
print('ahora se borrará todo')
sr.clearScreen(1)