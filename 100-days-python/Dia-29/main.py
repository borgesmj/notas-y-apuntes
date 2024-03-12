def newPrint(color, text):
  if color == "yellow":
    print("\033[1;33m", text, end='', sep=' ')
  elif color == "purple":
    print("\033[0;35m", text, end='', sep=' ')
  elif color == "red":
    print("\033[0;31m", text, end='', sep=' ')
  elif color == "blue":
    print("\033[0;34m", text, end='', sep=' ')
  else:
    print("\033[?25l", end='')

newPrint("yellow", "Super Subroutine")
print("\n")
newPrint("yellow", "With my")
newPrint("purple", "new program")
newPrint("yellow", 'I can just call red("and")')
newPrint("red", "and")
newPrint("yellow", "that word will appear in the color I set it to.")
print("\n")
newPrint("yellow", "with no")
newPrint("blue", "weird gaps.")
print("\n")
newPrint("yellow", "Epic.")
