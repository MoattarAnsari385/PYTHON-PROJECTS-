import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high :
            number = random.randint(low, high)
        else:
            number = low
        feedback = input(f"Is {number} is too high (H) and too low (L) or correct (C): ").lower()
        if feedback == "" or feedback.isspace():
            print("Invalid input. Blank spaces are not allowed. Please enter H, L, or C.")
            continue
        if feedback == "h":
            high = number -1
        elif feedback == "l":
            low = number +1
    print(f"yay, The computer the number, {number}, correctly ")

computer_guess(25)