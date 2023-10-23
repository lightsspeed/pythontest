import random

rps_game = ("r" , "p" , "s")

def rps():
    print("welcome to the RPS game")
    score_user = 0
    score_comp = 0

    while True:
        user = input("Choose R/P/S: ").lower()
        if user not in ["r" , "p" , "s"]:
            print("Invalid input. Please enter r/p/s")
            continue
            
        
        comp = random.choice(rps_game)
        print("user choice is", user)
        print("comp choice is", comp)

        if user == comp:
            print("It is a Tie.")
        elif (user == "r" and comp == "s") or (user == "p" and comp == "r") or (user == "s" and comp == "p"):
            print("User wins!!")
            score_user += 1
        else:
            print("Comp wins!!")
            score_comp += 1
        
        print("user score is ", score_user)
        print("comp score is ", score_comp)
        
        if score_comp == 5 or score_user ==5:
            break
    if score_user > score_comp:
        print("user wins!!")
    else:
        print("comp wins!!")
rps()

