class character:
  name = None
  health = None
  magic_points = None

  def __init__(self, name, health, magic_points):
    self.name = name
    self.health = health
    self.magic_points = magic_points


class player(character):
  lives = None
  its_alive = None

  def __init__(self, name, health, magic_points, lives, its_alive):
    self.name = name
    self.health = health
    self.magic_points = magic_points
    self.lives = lives
    self.its_alive = its_alive

  def print(self):
    print('== Character == ')
    print(f"""
    Name: {self.name}
    Health: {self.health}
    Magic Points: {self.magic_points}
    Lives: {self.lives}
    Its Alive: {self.its_alive}
    """)

class enemy(character):
  type = None

  def __init__(self, name, health, magic_points, type):
    self.name = name
    self.health = health
    self.magic_points = magic_points
    self.type = type

class vampire(enemy):
  strength = None
  day_nigth = None

  def __init__(self, name, health, magic_points, strength, day_nigth):
    self.name = name
    self.health = health
    self.magic_points = magic_points
    self.type = "Vampire"
    self.strength = strength
    self.day_nigth = day_nigth

  def print(self):
    print('== Enemy == ')
    print(f"""
    Name: {self.name}
    Health: {self.health}
    Magic Points: {self.magic_points}
    Type: {self.type}
    Strength = {self.strength}
    Day or Nigth: {self.day_nigth}
    """)

class ogre(enemy):
  strength = None
  speed = None

  def __init__(self, name, health, magic_points, strength, speed):
    self.name = name
    self.health = health
    self.magic_points = magic_points
    self.type = "Ogre"
    self.strength = strength
    self.speed = speed

  def print(self):
    print('== Enemy == ')
    print(f"""
    Name: {self.name}
    Health: {self.health}
    Magic Points: {self.magic_points}
    Type: {self.type}
    Strength = {self.strength}
    Speed: {self.speed}
    """)
    
player = player("David", 100, 50, 3, True)
boris = vampire("Boris", 45, 70, 3, "Nigth")
rishi = vampire("Rishi", 70, 10, 75, "day")
ted_ted = ogre("Ted Ted", 75, 40, 80, 90)
bill = ogre("Bill", 60, 5, 75, 90)
station = ogre("Station", 35, 40, 49, 50)
player.print()
boris.print()
rishi.print()
ted_ted.print()
bill.print()
station.print()