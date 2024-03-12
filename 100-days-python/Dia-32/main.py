import random

greetings = [
  "Buenos dias",
  "Good Morning",
  "Aloha kakahiaka",
  "God morgen",
  "Guten Morgen",
  "Բարի առավոտ",
  "おはよう",
  "Bonjour",
  "Hyvää huomenta"
]

index = random.randint(0, len(greetings) - 1)

print(f"{greetings[index]}")