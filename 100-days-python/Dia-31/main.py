def colorChange(color):
  if color == 'yellow':
      return ("\033[1;33m")
  elif color == 'blue':
      return ("\033[0;34m")
  elif color == 'red':
      return ("\033[0;31m")
  elif color == 'green':
      return ("\033[1;32m")
  elif color == 'purple':
    return ("\033[1;32m")
  else:
      return "\033[0m"

title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}={colorChange('yellow')} Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="
player = f"""
🔥▶️ \t{colorChange('white')}Radio Gaga\n\t\t{colorChange('yellow')}Queen
"""
prev = 'PREV'
next = 'NEXT'
pause = 'PAUSE'

welcome = f"{colorChange('white')}WELCOME TO"
armbook = f"{colorChange('blue')}-- ARMBOOK --"
message_1 = f"{colorChange('yellow')}Definitely not a rip off of"
message_2 = f"{colorChange('yellow')}a certain other social"
message_3 = f"{colorChange('yellow')}networking site."
honest = f"{colorChange('red')}Honest."
username = f"{colorChange('white')}Username:"
password = f"{colorChange('white')}Password:"


print(f"        {title:^35}")  
print()
print(player)
print()
print(f"{colorChange('white')}{prev:<35}")
print(f"{colorChange('green')}{next:^35}")
print(f"{colorChange('purple')}{pause:>35}")
print()
print(f"{welcome:^35}")
print(f"{armbook:^35}")
print(f"{message_1:>35}")
print(f"{message_2:>35}")
print(f"{message_3:>35}")
print()
print(f"{honest:^35}")
print()
print(f"{username:^35}")
print(f"{password:^35}")


