for i in range(1, 31):
  user_opinion = input(f"¿Que te parecio el dia {i}:\n")
  print()
  texto = f"Pensaste que el dia {i} fue {user_opinion:>3}"
  print(f"{texto:^3}")
  print()

