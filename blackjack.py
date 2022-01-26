import random
import os

from time import sleep 
cmd = 'mode 70,12'
os.system(cmd)

def play_game():
    player_turn = True
    dealer_turn = False
    chips = 10000
    hand_count = 0
    print ("≣" * 24,"[BLACKJACK]", "≣" * 24)
    deck = build_deck()
    deck = burn_cards(deck)
    while len(deck) > 40 and chips > 0:
            player_turn = True
            print (f"Remaining cards [{len(deck)}] | Chips [{chips}] | Hands played [{hand_count}]")
            bet, chips = bet_amount(chips)
            player_hand, dealer_hand, deck, hand_count = deal_hands(deck,hand_count)
            player_score, dealer_score = get_current_scores(player_hand,dealer_hand)
            display_hands(player_hand,dealer_hand,player_score,dealer_score,dealer_turn,deck,hand_count,chips)
            while player_turn == True:
                player_hand,deck,player_turn,stand = player_choice(player_hand,deck)
                player_score, dealer_score = get_current_scores(player_hand,dealer_hand)
                display_hands(player_hand,dealer_hand,player_score,dealer_score,dealer_turn,deck,hand_count,chips)
                player_turn,dealer_turn,bust = check_player_score(player_score,stand)
            while dealer_turn == True:
                player_score, dealer_score = get_current_scores(player_hand,dealer_hand)
                sleep(1)
                display_hands(player_hand,dealer_hand,player_score,dealer_score,dealer_turn,deck,hand_count,chips)                    
                dealer_turn,chips = check_hands(bust,dealer_score,player_score,bet,chips)                 
                dealer_hand,deck = dealer_choice(dealer_hand,dealer_score,deck)
    print ("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print (f"You scored {chips}")
    play_yn = ["y","n"]
    play_again = ""
    while play_again not in play_yn:
        play_again = input("Play again ? y/n : ")
    if play_again == "y":
        print ("\n"*12)
        play_game()
    else:
        exit
def check_hands(bust,dealer_score,player_score,bet,chips):
    dealer_turn = True
    if bust == True:
        print (f"==DEALER WINS = PLAYER BUSTS = -{bet}==")
        dealer_turn = False
    if sum(player_score) > sum(dealer_score) and sum(dealer_score) > 16 and sum(player_score) < 21:
        print (f"==PLAYER WINS = HIGH SCORE = +{bet*2}==")
        chips = (chips + ( bet * 2))
        dealer_turn = False
    if sum(dealer_score) > 21:
        print (f"==PLAYER WINS = DEALER BUSTS = +{(bet*2)}==")
        chips = (chips + ( bet * 2))
        dealer_turn = False
    if sum(dealer_score) > sum(player_score) and sum(dealer_score) < 22 and sum(dealer_score) > 16:
        print (f"==DEALER WINS = HIGH SCORE = -{bet}==")
        dealer_turn = False
    if sum(dealer_score) > 16 and sum(dealer_score) == sum(player_score):
        print (f"==PUSH = + {bet}==")
        chips = (chips + bet)
        dealer_turn = False
    if sum(player_score) == 21 and len(player_score) > 2 and sum(dealer_score) > 16 and sum(dealer_score) < sum(player_score):
        print (f"==PLAYER WINS = HIGH SCORE = +{bet*2}==")
        chips = (chips + bet*2)
        dealer_turn = False

    if dealer_turn == False:
        sleep(1)    
    return dealer_turn,chips
    
def dealer_choice(dealer_hand,dealer_score,deck):
    if sum(dealer_score) < 17:
        card_index = random.randint(0,len(deck)-1)
        dealer_hand.append(deck[card_index])
        deck.pop(card_index)
    return dealer_hand,deck
    
def check_player_score(player_score,stand):
    bust = False
    if sum(player_score) == 21:
        player_turn = False
        dealer_turn = True
    if sum(player_score) > 21:
        player_turn = False
        dealer_turn = True
        bust = True
    if stand == True:
        player_turn = False
        dealer_turn = True
    if sum(player_score) < 21 and stand == False:
        player_turn = True
        dealer_turn = False
    return player_turn,dealer_turn,bust

def player_choice(player_hand,deck):
    choices = ["hit","stand"]
    choice = ""
    stand = False
    while choice not in choices:
        choice = str(input("hit or stand: "))
    if choice == "hit":              
        card_index = random.randint(0,len(deck)-1)
        player_hand.append(deck[card_index])
        deck.pop(card_index)
        player_turn = True
    if choice == "stand":
        player_turn = False
        stand = True
    return player_hand,deck,player_turn,stand

def get_current_scores(player_hand,dealer_hand):
    remove_suits = str.maketrans("","","♠♥♦♣")
    player_score = [string.translate(remove_suits) for string in player_hand]
    dealer_score = [string.translate(remove_suits) for string in dealer_hand]
    player_score = [string.replace("J","10").replace("Q","10").replace("K","10").replace("A","11") for string in player_score]
    dealer_score = [string.replace("J","10").replace("Q","10").replace("K","10").replace("A","11") for string in dealer_score]
    player_score = list(map(int,player_score))
    dealer_score = list(map(int,dealer_score))
    if 11 in player_score:
        while sum(player_score) > 21 and 11 in player_score:
            player_score[player_score.index(11)] = 1     
    if 11 in dealer_score:
        while sum(dealer_score) > 21 and 11 in dealer_score:
            dealer_score[dealer_score.index(11)] = 1    
    return player_score, dealer_score

def display_hands(player_hand,dealer_hand,player_score,dealer_score,dealer_turn,deck,hand_count,chips):
    hold_dealer_2nd_card = dealer_hand[1]
    print ("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    top_card_slice = "╔═══╗"
    bottom_card_slice = "╚═══╝"
    middle_spacer = "|"
    print ("==PLAYER==", "Hand value:",sum(player_score))
    print (top_card_slice * len(player_hand))   
    for card in player_hand:
        if len(card) > 2:
            space = ""
        else:
            space = " "
        print ("║"+card+space+"║", end="")
    print ()
    print (bottom_card_slice * len(player_hand))
    if dealer_turn == False:
        dealer_hand[1] = "  "
    print ("==DEALER==", "Hand value: ",end="")
    if dealer_turn == False:
        print ("?")
    else:
        print (sum(dealer_score))
    print (top_card_slice * len(dealer_hand))
    for card in dealer_hand:
        if len(card) > 2:
            space = ""
        else:
            space = " "
        print ("║"+card+space+"║", end="")
    print ()
    print (bottom_card_slice * len(dealer_hand))
    dealer_hand[1] = hold_dealer_2nd_card

def deal_hands(deck,hand_count):
    player_hand = []
    dealer_hand = []
    hand_count += 1
    while len(player_hand) != 2:
        card_index = random.randint(0,len(deck)-1)
        player_hand.append(deck[card_index])
        deck.pop(card_index)
    while len(dealer_hand) != 2:
        card_index = random.randint(0,len(deck)-1)
        dealer_hand.append(deck[card_index])
        deck.pop(card_index)
    return player_hand, dealer_hand, deck, hand_count

def bet_amount(chips):
    bet = 0
    while not int(bet) in range (1,chips+1):
        try:
            bet = int(input("Enter bet amount: "))
        except ValueError:
            print (f"Bet amount must be in range [1 - {chips}]")
    chips = chips - bet
    return bet, chips    
                        
def build_deck():
    deck = []
    x = 0
    card_value = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    card_suit = ["♠","♥","♦","♣"]
    deck_amount = 0
    while not int(deck_amount) in range(1,10):
        try:
            deck_amount = int(input("How many decks? [1 - 9] :  " ))
        except ValueError:
            print ("Enter a number between [1 - 9]")
    while len(deck) != (52*deck_amount):
        for i in card_value:
            card = str(i) + card_suit[x]
            deck.append(card)
        x +=1
        if x == 4:
            x = 0
    return deck

def burn_cards(deck):
    amount_to_burn = 6
    removed_cards = []
    while not int(amount_to_burn) in range (0,6):
        try:
            amount_to_burn = int(input("Would you like to burn any cards? [0 - 5] : "))
        except ValueError:
            print ("Burn amount must be in range [0 - 5]")
    while amount_to_burn > 0:
        card_removed = random.randint(0,len(deck)-1)
        removed_cards.append(deck[card_removed])
        deck.pop(card_removed)
        amount_to_burn -= 1
    if len(removed_cards) > 0:
        print ("The following card(s) have been removed", *removed_cards,sep=" ")
    return deck

play_game()
