import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Please enter a positive number.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def display_password(password):
    print("\nGenerated Password: ", password)

def main():
    length = get_password_length()
    password = generate_password(length)
    display_password(password)

if __name__ == "__main__":
    main()
