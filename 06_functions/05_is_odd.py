def is_odd(num:int):
    remainder = num % 2
    return remainder == 1

for i in range(10):
    if is_odd(i):
        print(i, end = " ")
        print("Odd")
    else:
        print(i, end = " ")
        print("even")