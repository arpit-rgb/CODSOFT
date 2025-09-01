# password_generator.py

import random
import string

def generate_password(length):
    # Combine letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password should be at least 4 characters long.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    password = generate_password(length)
    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
