import random
from time import sleep

def play_game():
    print ("≣" * 20,"[BLACKJACK]", "≣" * 20)
    deck = build_deck()
    chips = choose_starting_chips()
    deck = burn_cards(deck)
    hand_count = 0
    while chips > 0:
        turn = True
        busted = False
        stand = False     
        if len(deck) < 5:
            print ("Game over")
            break
        print (f"Remaining cards [{len(deck)}] | Chips [{chips}] | Hands played [{hand_count}]")
        bet, chips = bet_amount(chips)
        player_hand, dealer_hand, deck, hand_count = deal_hands(deck,hand_count)
    ##    player_hand = ["A♠","5♠"]
        player_score, dealer_score = get_current_scores(player_hand,dealer_hand)
        while turn == True:
            print (f"Remaining cards [{len(deck)}] | Chips [{chips}] | Hands played [{hand_count}]")
            display_hands(player_hand,dealer_hand,turn,player_score,dealer_score)
            player_hand, player_score,deck,turn,stand = player_turn( player_hand, player_score, deck,stand)
            player_score, dealer_score = get_current_scores(player_hand,dealer_hand)
            turn, busted, stand = check_player_score(player_score,busted,stand)


        while turn == False:
            if busted == True:
                display_hands(player_hand,dealer_hand,turn,player_score,dealer_score)
                print ("==PLAYER BUSTED==")
                input("Press enter for next hand")
                turn = True
            if stand == True:
                display_hands(player_hand,dealer_hand,turn,player_score,dealer_score)
                sleep(1)
                while sum(dealer_score) <= 16:
                    dealer_hand, dealer_score, deck = dealer_turn(dealer_hand,dealer_score,deck)
                    player_score, dealer_score = get_current_scores(player_hand,dealer_hand)
                    display_hands(player_hand,dealer_hand,turn,player_score,dealer_score)
                    sleep(1)
                    
                if sum(dealer_score) == sum(player_score):
                    chips = chips + bet
                    round_msg = "==PUSH=="
                if sum(dealer_score) > sum(player_score) and sum(dealer_score) <= 21:
                    round_msg = "==DEALER WINS=="
                if sum(player_score) > sum(dealer_score):
                    round_msg = "==PLAYER WINS=="
                    chips = chips + (bet * 2)
                elif sum(dealer_score) > 21:
                    round_msg = "==DEALER BUSTS=="
                    chips = chips + (bet * 2)                
                display_hands(player_hand,dealer_hand,turn,player_score,dealer_score)
                print (round_msg)
                turn = True
                input("Press enter for next hand")
                print ("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")

def dealer_turn(dealer_hand,dealer_score,deck):
    card_index = random.randint(0,len(deck)-1)
    dealer_hand.append(deck[card_index])
    deck.pop(card_index)
    return dealer_hand, dealer_score, deck

def build_deck():
    deck_amount = 0
    while not int(deck_amount) in range(1,10):
        try:
            deck_amount = int(input("How many decks? [1 - 9] :  " ))
        except ValueError:
            print ("Enter a number between [1 - 9]")
    deck = []
    x = 0
    card_value = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    card_suit = ["♠","♥","♦","♣"]
    while len(deck) != (52*deck_amount):
        for i in card_value:
            card = str(i) + card_suit[x]
            deck.append(card)
        x +=1
        if x == 4:
            x = 0
    return deck

def choose_starting_chips():
    chips = 0
    while not int(chips) in range(1,10001):
        try:
            chips = int(input("Amount of starting chips [1 - 10000] : "))
        except ValueError:
            print ("Starting chips must be in range [1 - 10000]")
    return chips

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

def display_hands(player_hand,dealer_hand,turn,player_score,dealer_score):
    dealer_hand_hold = dealer_hand[1]
    top_card_slice = "╔═══╗"
    bottom_card_slice = "╚═══╝"
    middle_spacer = "|"
    if turn == True:
        dealer_hand[1] = "  "
    print ("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
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
    print ("==DEALER==", "Hand value: ", end="")
    if turn == True:
        print (dealer_score[0])
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
    dealer_hand[1] = dealer_hand_hold
    
def get_current_scores(player_hand,dealer_hand):
    suits = "♠♥♦♣"
    player_score = []
    dealer_score = []
    for card in player_hand:
        temp =""
        for bit in card:
            if bit not in suits:
                if bit == "J" or bit == "Q" or bit == "K":
                    bit = "10"
                if bit == "A":
                    bit = "11"                   
                temp += bit
                if temp == "  ":
                    temp = 0                  
        player_score.append(int(temp)) 
    for card in dealer_hand:
        temp =""
        for bit in card:
            if bit not in suits:
                if bit == "J" or bit == "Q" or bit == "K":
                    bit = "10"
                if bit == "A":
                    bit = "11"
                temp += bit
                if temp == "  ":
                    temp = 0
        dealer_score.append(int(temp))
    return player_score, dealer_score

def player_turn(player_hand,player_score,deck,stand):
    choices = ["hit","stand"]
    choice = ""
    while choice not in choices:
        choice = str(input("hit or stand: "))
    if choice == "hit":              
        card_index = random.randint(0,len(deck)-1)
        player_hand.append(deck[card_index])
        deck.pop(card_index)
        turn = True
    if choice == "stand":
        turn = False
        stand = True
    return player_hand,player_score,deck,turn,stand

def bet_amount(chips):
    bet = 0
    while not int(bet) in range (1,chips+1):
        try:
            bet = int(input("Enter bet amount: "))
        except ValueError:
            print (f"Bet amount must be in range [1 - {chips}]")
    chips = chips - bet
    return bet, chips

def check_player_score(player_score,busted,stand):
    if sum(player_score) < 21:
        turn = True
    if sum(player_score) == 21:
        turn = False
        stand = True
    if sum(player_score) > 21:
        busted = True
        turn = False
    elif stand == True:
        turn = False
    return turn, busted, stand

##def check_hand_for_ace(player_hand,player_score,busted,turn):
##    for card in player_hand:
##        if "A" in card:
##            player_score_2 = sum(player_score) - 10
##    if busted == True:
##       # player_score = player_score_2
##
##        busted == False
##        turn = True
##        
##    return player_score, player_score_2, busted, turn
            

play_game()

