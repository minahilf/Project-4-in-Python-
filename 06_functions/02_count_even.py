def count_even():
    numbers= []

    while True:
        user_num = input("Enter number or press enter to stop: ")
        if user_num == "":
            break

        num = int(user_num)
        numbers.append(num)

    even_count = 0
    for n in numbers:
        if n % 2 == 0:
            even_count += 1

    print(f"Numbers of even numbers: {even_count}")

count_even()