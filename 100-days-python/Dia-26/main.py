from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # reproducir el audio
  while True:
    stop_playback = int(input("Presione 2 para detener la reproducion > "))
    if stop_playback == 2:
      source.paused = True; # pausar el audio 
      return
    else:
      continue

while True:
  os.system('clear')
  time.sleep(1)
  print("🎵 MyPOD Music Player")
  time.sleep(1)
  print("Presiona 1 para reproducir")
  time.sleep(1)
  print("Presiona 2 para Salir")
  time.sleep(1)
  print()
  print("Presiona otro numero para ver el menu de nuevo")
  opcion = int(input("> "))
  if(opcion == 1):
    time.sleep(1)
    print("Reproduciendo...")
    play()
  elif(opcion == 2):
    time.sleep(1)
    print('Adios')
    exit()
  else:
    continue

