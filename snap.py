import random
import time
from time import sleep
def play_game():
    sleep(3)
    animal_list = open('animals.txt').read().splitlines()
    animal_list_len = len(animal_list)-3
    round_count = 0
    cards = []
    score = 0
    cards = build_first_go(animal_list,cards)
    start_time = time.time()
    acc_tracker = 0
    while len(animal_list) > 1:
        print ()
        print (f"SCORE: {score} | Remaining", len(animal_list)-2)
        print (cards)
        player_choice = input("SNAP? y/n :")
        score,acc_tracker = check_snap(cards,player_choice,score,acc_tracker)
        cards = next_cards(cards,animal_list)
    finish_time = time.time()
    print ()
    if acc_tracker > 0:
        acc_tracker = ((float(acc_tracker)/float(animal_list_len))*100)
    else:
        acc_tracker = 0
    print (f"Your score was {score} in {finish_time -start_time:0.2f} seconds | Accuracy : {acc_tracker:0.2f}%")

def next_cards(cards,animal_list):
    cards[0] = cards[1]
    index_card = random.randint(1,len(animal_list)-1)
    word = animal_list[index_card]
    cards[1] = word
    animal_list.pop(index_card)
    return cards
        
def check_snap(cards,player_choice,score,acc_tracker):
    if player_choice == "y":
        if cards[0] == cards[1]:
            score += 1
            acc_tracker +=1
        else:
            score -= 1
    if player_choice == "n":
        if cards[0] == cards[1]:
            score -=1
        else:
            acc_tracker += 1
    return score,acc_tracker

def build_first_go(animal_list,cards):
    while len(cards) < 2:
        index_card = random.randint(1,len(animal_list)-1)
        word = animal_list[index_card]
        cards.append(word)
        animal_list.pop(index_card)
    return cards

play_game()
