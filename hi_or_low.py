# Guess My Number
# The computer picks a random number
import random
lives = 3
card = random.randint(1,13)
def play_game(lives,card):
    guess_score = ""
    score = 0
    new_card = 0
    while lives > 0:
        guess_score == False
        print (f"\nhi lo or ti? Current lives: {lives} | Current score {score} | Current card: {card}")
        guess = input("Hi or lo: ")
        new_card = random.randint(1,13)
        while new_card == card:
            new_card = random.randint(1,13)
        if str(guess) == "hi":
            if new_card > card:
                score +=1
        if str(guess) == "lo":
            if new_card < card:
                score +=1
        if str(guess) == "hi":
            if new_card < card:
                lives -=1
        if str(guess) == "lo":
            if new_card > card:
                lives -=1
        card = new_card
    print (f"Your score was {score}")
play_game(lives,card)
 
 

