# Python Project 3: Random Password Generator
# Name: Nazish Ajaz

import random
import string

MIN_LENGTH = 4
MAX_LENGTH = 100

print("===== RANDOM PASSWORD GENERATOR =====")

while True:
    try:
        # Get password length
        length = int(input("Enter password length: "))

        if length < MIN_LENGTH or length > MAX_LENGTH:
            print(f"Please enter a length between {MIN_LENGTH} and {MAX_LENGTH}.")
            continue

        # Characters to use
        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        # Generate password
        password = "".join(
            random.choice(characters)
            for _ in range(length)
        )

        print("\nGenerated Password:", password)

        # Validate y/n input
        while True:
            again = input("\nGenerate another password? (y/n): ").lower()

            if again == "y":
                break

            elif again == "n":
                print("Thank you for using Password Generator!")
                exit()

            else:
                print("Please enter only y or n.")

    except ValueError:
        print("Please enter a valid number.")