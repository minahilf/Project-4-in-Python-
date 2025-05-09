MAX_LENGTH:int = 5

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)

def create_lst():

    lst = []
    elem = input("Enter element or press enter to stop: ")
    
    while elem != "":
        lst.append(elem)
        elem = input("Enter element or press enter to stop: ")
    return lst

def main():
    lst = create_lst()

    shorten(lst)

if __name__ == "__main__":
    main()
