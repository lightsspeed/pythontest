import random

print("Welcome to the dice game")

def roll_dice():
    score = 0
    
    while score < 50:
        roll = input("Do you want to roll a dice (y/n): ")
        
        if roll.lower() == "n":
            break
        elif roll.lower() != "y":
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        
        dice = random.randint(1, 6)
        
        if dice == 1:
            print("Dice rolled is {}. Game ended, score is zero".format(dice))
            break
        else:
            score += dice
            print("Dice rolled is {} and score is {}".format(dice, score))

    if score >= 50:
        print("Congratulations! You've won the game!")
    else:
        print("Game ended. Your final score is:", score)

roll_dice()
