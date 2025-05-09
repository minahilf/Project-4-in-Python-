def in_stock(fruit):
    if fruit == "apple":
        return 10
    elif fruit == "pineapple":
        return  6
    elif fruit == "kiwi":
        return 99
    else:
        return 0

fruit = input("Enter fruit: ")
fruits = in_stock(fruit)
if fruits == 0:
    print('This fruit is not in stock')
else:
    print("This fruit is in stock! Here is how many:")
    print(fruits)