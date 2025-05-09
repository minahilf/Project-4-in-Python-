def get_element(lst):
    print(f"Here is your list: {lst})

def create_lst():

    lst = []
    elem = input("Enter element or press enter to stop: ")
    
    while elem != "":
        lst.append(elem)
        elem = input("Enter element or press enter to stop: ")
    return lst

def main():
    lst = create_lst()

    get_element(lst)

if __name__ == "__main__":
    main()
