from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()


def login(email, password, stored_data):
    hashed = hash_password(password)

    if email in stored_data:
        if stored_data[email] == hashed:
            return True
    return False

def main():
    stored_data = {
        "minahil@gmail.com": hash_password("samosa123"),
        "ahmed@code.com": hash_password("nextjs"),
    }

    email = input("Enter Email: ")
    password = input("Enter Password: ")

    if login(email, password, stored_data):
        print("Login successful!")
    else:
        print("Login failed")

if __name__ == "__main__":
    main()
