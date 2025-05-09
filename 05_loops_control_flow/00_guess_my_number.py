import random

random_number = random.randint(0,99)

your_num = int(input("Guess the number: "))

while your_num != random_number:
    if your_num < random_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    
    print()
    your_num = int(input("Guess the new number: "))

print(f"Congrats your guess is correct The number was {random_number}")
