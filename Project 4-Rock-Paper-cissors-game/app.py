import random

def play():
    user = input("What's your choise? 'r' for Rock, 'p' for Paper, and 's' for Scissors: ")
    computer = random.choice(['r', 'p', 's'])

    
    if user == computer:
        return "It\'s Tie"

    if isWin (user,computer):
        return "You Won"
    return "You Lost!"

def isWin(player, opponent):
    if (player == "r" and opponent == "s" ) or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(play())
