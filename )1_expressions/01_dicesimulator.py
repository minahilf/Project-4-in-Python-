import random
def Game():
  dice = 3
  for i in range(dice):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print(f"Roll {i + 1}: Die 1 = {roll1}, Die 2 = {roll2}")
    print(f"Total is {roll1 + roll2}")
Game()