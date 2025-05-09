def in_range(n,low,high):
    if n >= low and n <= high:
        return True
    return False

n = int(input("Enter number: "))
low = int(input("Enter lowest number: "))
high = int(input("ENter highest number: "))

print(in_range(n,low,high))