ADULT = 18

def is_adult(age):
    if age > ADULT:
        return True
    return False

def main():
    age = int(input("How old is this person? "))
    print(is_adult(age))

if __name__ == "__main__":
    main()