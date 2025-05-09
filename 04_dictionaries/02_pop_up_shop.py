fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}

total = 0

for fruit_names in fruits:
    price = fruits[fruit_names]
    fruit_bought = int(input(f"How many {fruit_names} you want? "))
    total += (price * fruit_bought)

print(f"Your Total amount is $ {str(total)}")