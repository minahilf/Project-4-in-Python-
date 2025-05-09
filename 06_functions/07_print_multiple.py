def print_multiple(msg: str,repeat:int):
    repeated_msg = (msg + " ") * repeat
    print(repeated_msg)

message = input("Enter message: ")
repeat = int(input("Enter number you want to repeat the message: "))

print_multiple(message, repeat)

