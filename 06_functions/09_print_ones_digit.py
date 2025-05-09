def print_ones(num):
    print(f"The ones digit is {num%10}")

def main():
    num = int(input("Enter number: "))
    print_ones(num)

if __name__ == "__main__":
    main()