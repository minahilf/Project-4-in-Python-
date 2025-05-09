def read_phone_numbers():
    phonebook = {}

    while True:
        name = input("Enter name or press enter to stop: ")
        if name == "":
            break
        number = input("Enter number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")

def search_number(phonebook):
    while True:
        search_name = input("Enter name: ")

        if search_name == "":
            break

        if search_name not in phonebook:
            print(f"{search_name} is not in phonebook")
        else:
            print(f"Number: {phonebook[search_name]}")

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    search_number(phonebook)


if __name__ == '__main__':
    main()