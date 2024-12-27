import random

def number_guess(x):
    number = random.randint(1 , x)
    guess = 0

    while guess != number:
        guess = int(input("Guess a number: "))
        if guess < number:
            print("Too low. Try again!")
        elif guess > number:
            print("Too high. Try again!")
    print(f"Congratulations! You guessed the number {number} correctly!")

number_guess(100)