myList = []


def printList():
  print()
  for i in myList:
    print(i)
  print()


while True:
  first_name = input("Nombre > ").strip().upper()
  last_name = input("Apellido > ").strip().upper()
  full_name = (f"{first_name} {last_name}")
  if full_name not in myList:
    myList.append(full_name)
  else:
    print("error, duplicado")
  printList()
