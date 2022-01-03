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

### Random lists into 1 list no dupes ####
##import random
##list_a = []
##list_b = []
##while len(list_a) < 25:
##    random_int = random.randint(1,50)
##    list_a.append(random_int)
##while len(list_b) < 25:
##    random_int = random.randint(1,50)
##    list_b.append(random_int)
##def list_compare(a,b):
##    list_c = []
##    for number in list_a:
##        if number in list_b:
##            if number != list_c:
##                list_c.append(number)
##    return list_c
##print ("List A:",list_a)
##print ("List B:",list_b)
##print ("List C:",list_compare(list_a,list_b))

### Prime number check ###
##number = input("Enter a number: ")
##def is_number_prime(number):    
##    list_a = [*range(2,number - 1,1)]
##    for num in list_a:
##        if number % num == 0:
##            print ("Number is not prime")
##            return number
##            break
##        else:
##            print ("Number is prime")
##            return number
##print (is_number_prime(int(number)))

### First and last ###
##import random
##list_a = []
##while len(list_a) < 50:
##    random_number = random.randint(1,100)
##    list_a.append(random_number)
##list_b = [list_a[0], list_a[-1]]
##print (list_b)

### Fib sequence ###
##amount_of_num = input("How many fibonnaci numbers to generate? ")
##def fib_stuff(amount_of_num):
##    count = 0
##    n1, n2 = 1, 1
##    new_list = []
##    while count < int(amount_of_num):
##        new_list.append(n1)
##        nth = n1 + n2
##        n1 = n2
##        n2 = nth
##        count += 1
##    return new_list
##print (fib_stuff(amount_of_num))

### New list - No dupes 
##import random
##list_a =[]
##while len(list_a) < 25:
##    list_a.append(random.randint(1,10))
##print (list_a)
##def no_dupes(list_a):
##    list_b = []
##    for num in list_a:
##            if num not in list_b:
##                list_b.append(num)
##    return list_b
##print (no_dupes(list_a))

### Backwards Input ###
##user_string = input("Please enter a sentence: ")
##def sentence_backwards(user_string):
##    string = user_string.split()
##    new_sentence = []
##    for word in string:
##        new_sentence.insert(0,word)
##    return new_sentence
##print (sentence_backwards(user_string))

### Password gen ###
##import random
##password_len = input("Length of password? (Between 8 - 20): ")
##if int(password_len) > 20 or int(password_len) < 8:
##    password_len = input("Length of password? (Between 8 - 20): ")
##char = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
##def password_gen(password_len):
##    password = "".join(random.sample(char,int(password_len)))
##    return password
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

### Bulls and Cows Game ####
##import random
##random_number = str(random.randint(1000,9999))
##guess = 0
##guess_count = 0
##cows = 0
##bulls = 0
##while int(guess) != random_number:
##    print ("Cows:",cows, " Bulls:",bulls, " Guesses:",guess_count)
##    x = 1
##    cows = 0
##    bulls = 0
##    guess = input("Guess the number: ")
##    if int(guess) == int(random_number):
##        print ("You got it right! It was",guess)
##        break
##    if guess.isnumeric() == False:
##        guess = input("Please enter a 4 digit number: ")
##    while x < 5:
##        if guess[x-1:x] == random_number[x-1:x]:
##            cows += 1
##            x += 1
##        else:
##            x += 1
##            bulls += 1
##    guess_count += 1

### is number in the list? ####
##import random
##number = random.randint(1,25)
##number_list = []
##def is_in_list(number_list):
##    while len(sorted(number_list)) < 20:
##        number_list.append(random.randint(1,50))
##    number_list.sort()
##    for integer in number_list:
##        if integer == number:
##            return True
##    return False
##print (is_in_list(number_list))

##count_dict = {}
##
##with open("nameslist.txt", "r") as file:
##    name = file.readline()
##    while name:
##        name = name.strip()
##        if name in count_dict:
##            count_dict[name] +=1
##        else:
##            count_dict[name] = 1
##        name = file.readline()
##print (count_dict)

# new list comparing numbers in 2 text files ###
primelist = []
happylist = []
with open("primenumbers.txt","r") as primefile:
    prime_number = primefile.readline()
    while prime_number:
        prime_number = prime_number.strip()
        primelist.append(int(prime_number))
        prime_number = primefile.readline()                         
with open("happynumbers.txt","r") as happyfile:
    happy_number = happyfile.readline()
    while happy_number:
        happy_number = happy_number.strip()
        happylist.append(int(happy_number))
        happy_number = happyfile.readline()                        
newlist = []
for number in primelist:
    if number in happylist:
        newlist.append(number)
print (newlist)

# number guess vs computer ###
import random
your_number = input("Please enter a number between 1 and 100: ")

def computer(your_number):
    computer_guess = random.randint(1,100)
    guess_count = 1
    lower_bound = 1
    upper_bound = 100
    guess_list= []
    print ("The computer is going to try guess your number between 0 and 100")
    while computer_guess != int(your_number):
        print ("Computer guess: ",computer_guess, "Guess count: ", guess_count)
        guess_count += 1
        up_or_down = (input("Please enter high or low: "))
        if up_or_down == "+":
            upper_bound = computer_guess
            #computer_guess = random.randint(lower_bound,upper_bound - 1)
            computer_guess = (upper_bound -1 + lower_bound) // 2 
        else:
            lower_bound = computer_guess
            #computer_guess = random.randint(lower_bound + 1,upper_bound)
            computer_guess = (upper_bound + lower_bound +1) // 2    
    return "Your number is", computer_guess, "Guess count: ", guess_count         
print (computer(your_number))

## biggst int without using max() ###
import random
a = random.randint(1,1000)
b = random.randint(1,1000)
c = random.randint(1,1000)
def biggest_of_3(a,b,c):
    print (a,b,c)
    if a > b:
        biggest = a
    else:
        biggest = b
    if biggest > c:
        return biggest
    else:
        return c
print (biggest_of_3(a,b,c))

import random
def play_game():
    word = list((random.choice(open("sowpods.txt").read().split())))
    board_piece = "_" * len(word)
    board = list(board_piece)
    win_con = list(board_piece)
    guess_list = []
    guess_count = 6
    print (word)
    print ("Let's play hangman!")
    while word != win_con:
        if guess_count == 0:
            play_again = input("You lose, Play again? (y / n)")
            if play_again == "y":
                play_game()
            elif play_again == "n":
                break
        print ()
        print ("Board",*board)
        print ("Guess list:",*guess_list)
        print ("Guess_count:", guess_count)
        letter_guess = input("Guess a letter: ").upper()           
        if letter_guess in guess_list:
            letter_guess = ''
            print ("Already guessed")
            guess_count -= 1
        else:  
          for letter in word:
            if letter_guess not in guess_list:
                guess_list.append(letter_guess)
            if letter == letter_guess:
                index = word.index(letter_guess)
                board[index] = letter_guess
                word[index] = "_"
            if letter_guess not in guess_list and letter_guess in guess_list:
                guess_count -= 1
    else:
        print ("You win, the word is", "".join(board).lower())
        play_again = input("You win, Play again? (y / n)")
        if play_again == "y":
            play_game()
play_game()








