def Add_three_Copies(lst, data):
    for i in range(3):
        lst.append(data)

def main():
    word = input("Enter word: ")
    my_list = []
    print(f"Before: {my_list}")

    Add_three_Copies(my_list, word)

    print(f"after: {my_list}")

if __name__ == '__main__':
    main()