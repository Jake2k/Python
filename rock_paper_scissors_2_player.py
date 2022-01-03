# ROCK PAPER SCISSORS (2 Player) ###
games_won_player1 = 0
games_won_player2 = 0
while (games_won_player1 or games_won_player2 < 3):
    print ("Player 1: ", games_won_player1, " | Player 2: ", games_won_player2)
    player1 = input("Player 1: Rock, Paper or Scissors? ")
    player2 = input("Player 2: Rock, Paper or Scissors? ")
    if player1.lower() == player2.lower():
        print ("Tie")
    elif player1.lower() == "rock" and player2.lower() == "scissors":
        print ("Player 1 wins")
        games_won_player1 += 1
    elif player1.lower() == "rock" and player2.lower() == "paper":
        print ("Player 2 wins")
        games_won_player2 += 1
    elif player1.lower() == "scissors" and player2.lower() == "rock":
        print ("Player 2 wins")
        games_won_player2 += 1
    elif player1.lower() == "scissors" and player2.lower() == "paper":
        print ("Player 1 wins")
        games_won_player1 += 1
    elif player1.lower() == "paper" and player2.lower() == "scissors":
        print ("Player 2 wins")
        games_won_player2 += 1
    elif player1.lower() == "paper" and player2.lower() == "rock":
        print ("Player 1 wins")
        games_won_player1 += 1
    if games_won_player1 == 3:
        print ("Player 1 wins the match")
        print (games_won_player1, " : ", games_won_player2)
        break
    if games_won_player2 == 3:
        print ("Player 2 wins the match")
        print (games_won_player2, " : ", games_won_player1)
        break
