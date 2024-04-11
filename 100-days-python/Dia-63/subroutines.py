import time, os
def clearScreen(seconds):
  time.sleep(seconds)
  os.system('clear')

def turnRed(text):
  print("\033[0;31m",text)
