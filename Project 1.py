import random

print("Password Generator")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!%$&*#1234567890"

numbers = int(input("How Many Passwords Should Be Generated: "))

lenght = int(input("How many characters long: "))

for pwd in range(numbers):
    password = " "
    for c in range(lenght):
        control = password + random.choice(characters)
        password = control
        print(password)

print("YOU CAN CHOOSE FROM THESE PASSWORDS")


