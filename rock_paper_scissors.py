import random

def play_game():
    best_of = 0
    comp_select = 0
    comp_score = 0
    user_score = 0
    comp_roll = 0
    playing = False
    while int(best_of) not in [1, 3, 5]:
        best_of = input("Lets play Rock, Paper, Scissors, best out of 1, 3 or 5? ")
    print("You have chosen best of", best_of, ",Lets Play!")
    while playing is False:
        user_select = 0
        while str(user_select).lower() not in ["rock","paper","scissors"]:
            user_select = input("\nRock, Paper or Scissors? ")
            comp_roll = random.randint(1,3)
            if comp_roll == 1:
                comp_select = "rock"
            if comp_roll == 2:
                comp_select = "paper"
            else:
                comp_select = "scissors"
            print ("Computer chose: ",comp_select)
            if comp_select == user_select:
                print ("Tie")
            if comp_select == "rock" and user_select == "paper":
                user_score += 1
            if comp_select == "rock" and user_select == "scissors":
                comp_score += 1
            if comp_select == "paper" and user_select == "scissors":
                user_score += 1
            if comp_select == "paper" and user_select == "rock":
                comp_score += 1
            if comp_select == "scissors" and user_select == "rock":
                user_score += 1
            if comp_select == "scissors" and user_select == "paper":
                comp_score += 1
            print ("Computer: ",comp_score,"Player :",user_score)
            if int(comp_score) == int(best_of):
                winner = "Computer"
                playing = True
            if int(user_score) == int(best_of):
                winner = "Player"
                playing = True
    print ("-----------------------")
    print (winner, "wins this time!")
    return ""

print (play_game())
