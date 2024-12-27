import random

print("Welcome to your password generator!!")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-={}[]|;:'<>,.?/~0123456789"

number = int(input("Amount of password to generate: "))

length = int(input("Input your password length: "))

print("\nhere are your passwords: ")

for pwd in range(number):
    password = ""
    for i in range(length):
        password+=random.choice(chars)
    print(password)