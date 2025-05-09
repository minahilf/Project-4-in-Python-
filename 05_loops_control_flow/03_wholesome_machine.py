AFFIRMATION : str = "I am capable of doing anything I put my mind to."

print(f"Please type the following affirmation: {AFFIRMATION}")

user_msg = input()
while user_msg != AFFIRMATION:
    print("That was not affirmation")
    print(f"Please type the following affirmation: {AFFIRMATION}")
    user_msg = input()

print("That was right")

