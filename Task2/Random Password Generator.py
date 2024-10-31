import random
import string

print("Random Password Generator")

pwd = True
lth = True
while lth:
    length = int(input("Enter the password length (minimum 8): "))
    # Ensure minimum length of 8
    if length < 8:
        print("Password length must be at least 8.")
    else:
        print()
        lth = False

while pwd:

    print("Please select atleast one choice.")
    print("1 for Yes and 0 for No")
    print()
    letters = input("Do you want to add letters(1/0): ")
    numbers = input("Do you want to add numbers(1/0): ")
    special = input("Do you want to add special characters(1/0): ")

    # Validate that at least one character set is selected
    if letters != "1" and numbers != "1" and special != "1":
        print("Please select at least one character set!")
        print()
        pwd = True
    else:
        password_chars = ""

        if letters == "1":
            password_chars += string.ascii_letters
        if numbers == "1":
            password_chars += string.digits
        if special == "1":
            password_chars += string.punctuation

        # Generate the password
        generated_password = ''.join(random.choice(password_chars) for _ in range(length))

        print()
        print("Generated Password:", generated_password)
        pwd = False

