count = {}

num = input("Enter numbers or press enter to stop: ")
while num != "":
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
    num = input("Enter numbers or press enter to stop: ")

for numbers, times in count.items():
    print(f"{numbers} appears {times} times")

