### NAME AND AGE ###
##name = input("Give me your name: ")
##print (name)
##age = input("How old are you: ")
##years_to_age_100 = 100 - int(age)
##year_100 = 2019 + years_to_age_100
##print ("You are going to be 100 in the year " + str(year_100))

### EVEN OR ODD ###
##number = int(input("Please enter a number: "))
##if (number % 2) == 0:
##    print ("The number is even")
##else:
##    print ("The number is odd")

### List numbers < 5 filter ###
##list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##def list_less_than_5(list1):
##    less_than_5_list = [1]
##    for number in list1:
##        if number < 5:
##            less_than_5_list.append(number)
##    return less_than_5_list
##print (list_less_than_5(list1))

### List divisor of numbers ###
##number = int(input("Enter a number: "))
##divisor_list = []
##list_range = list(range(1,number+1))
##for integer in list_range:
##    if (number % integer) == 0:
##        divisor_list.append(integer)    
##print (divisor_list)

### List Filter non same ###
##a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
##def print_common(list_A,list_B):
##    list_C = []
##    for num in list_A:
##        if num in list_B:
##            if num != list_C:
##                list_C.append(num)
##    return list_C
##print (print_common(a,b))

### Word is palindrome ? ###
##word = input("Enter a palindrome: ")
##if word == word[::-1]:
##    print ("Word is a palinedrome")
##else:
##    print ("Word is not a palinedrome")
##a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
##new_list = []
##for num in a:
##    if (num % 2) == 0:
##        new_list.append(num)
##print (new_list)

### ROCK PAPER SCISSORS (2 Player) ###
##games_won_player1 = 0
##games_won_player2 = 0
##while (games_won_player1 or games_won_player2 < 3):
##    print ("Player 1: ", games_won_player1, " | Player 2: ", games_won_player2)
##    player1 = input("Player 1: Rock, Paper or Scissors? ")
##    player2 = input("Player 2: Rock, Paper or Scissors? ")
##    if player1.lower() == player2.lower():
##        print ("Tie")
##    elif player1.lower() == "rock" and player2.lower() == "scissors":
##        print ("Player 1 wins")
##        games_won_player1 += 1
##    elif player1.lower() == "rock" and player2.lower() == "paper":
##        print ("Player 2 wins")
##        games_won_player2 += 1
##    elif player1.lower() == "scissors" and player2.lower() == "rock":
##        print ("Player 2 wins")
##        games_won_player2 += 1
##    elif player1.lower() == "scissors" and player2.lower() == "paper":
##        print ("Player 1 wins")
##        games_won_player1 += 1
##    elif player1.lower() == "paper" and player2.lower() == "scissors":
##        print ("Player 2 wins")
##        games_won_player2 += 1
##    elif player1.lower() == "paper" and player2.lower() == "rock":
##        print ("Player 1 wins")
##        games_won_player1 += 1
##    if games_won_player1 == 3:
##        print ("Player 1 wins the match")
##        print (games_won_player1, " : ", games_won_player2)
##        break
##    if games_won_player2 == 3:
##        print ("Player 2 wins the match")
##        print (games_won_player2, " : ", games_won_player1)
##        break

### Guessing game one
##import random
##
##random_int = random.randint(1,9)
##guess = 0
##guess_count = 0
##
##while guess != random_int:
##    if int(guess_count) != 0:
##        print ("Guesses:",guess_count)
##    if int(guess) == 0:
##        guess = input("Guess the number between 1 and 9: ")
##    elif int(guess) == random_int:
##        print ("You guessed correct, it was", guess,"!")
##        break
##    elif int(guess) > random_int:
##        print ("You guessed to high, guess again")
##        guess = input("Guess the number between 1 and 9: ")
##        guess_count += 1
##    elif int(guess) < random_int:
##        print ("You guessed to low, guess again")
##        guess_count += 1
##        guess = input("Guess the number between 1 and 9: ")

# Random lists into 1 list no dupes ####
import random
list_a = []
list_b = []
while len(list_a) < 25:
    random_int = random.randint(1,50)
    list_a.append(random_int)
while len(list_b) < 25:
    random_int = random.randint(1,50)
    list_b.append(random_int)
def list_compare(a,b):
    list_c = []
    for number in list_a:
        if number in list_b:
            if number != list_c:
                list_c.append(number)
    return list_c
print ("List A:",list_a)
print ("List B:",list_b)
print ("List C:",list_compare(list_a,list_b))






##print (password_gen(password_len))

##import requests
##from bs4 import BeautifulSoup
## 
##base_url = 'http://www.nytimes.com'
##r = requests.get(base_url)
##soup = BeautifulSoup(r.text, "html.parser")
## 
##for story_heading in soup.find_all(class_="story-heading"): 
##    if story_heading.a: 
##        print(story_heading.a.text.replace("\n", " ").strip())
##    else: 
##        print(story_heading.contents[0].strip())

















