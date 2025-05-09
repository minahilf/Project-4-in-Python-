def get_last_element(lst):
    print(lst[-1])

def get_lst():

    lst = []
    elem = input("Enter element or press enter to pause: ")

    while elem != "":
        lst.append(elem)
        elem = input("Enter element or press enter to pause: ")

    return lst

def main():
    lst = get_lst()

    get_last_element(lst)

if __name__ == "__main__":
    main()