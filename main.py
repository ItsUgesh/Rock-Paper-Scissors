#UGESH
import random

computer = random.choice([-1, 0, 1])
compdict = {1: "Rock", 0: "Papper", -1: "Sicssors"}
ply_choice = input("Pleae select r, p, s => ")
plydict = {"r": 1, "p": 0, "s": -1}
choice = plydict[ply_choice]

print("Player choice:", compdict[choice])
print("Computer choice:", compdict[computer])

if computer == choice:
    print("Its Draw!👏  Play again")
else:
    if computer == 1 and choice == 0:
        print("You Win!😃👏 ")
    elif computer == 1 and choice == -1:
        print("You Lose!😔")
    elif computer == 0 and choice == 1:
        print("You Lose!😔")
    elif computer == 0 and choice == -1:
        print("You Win!😃👏 ")
    elif computer == -1 and choice == 1:
        print("You Wim!😃👏 ")
    elif computer == -1 and choice == 0:
        print("You Lose!😔")
    else:
        print("Somrthing went wrong or user choosed wrong Alphabet")
