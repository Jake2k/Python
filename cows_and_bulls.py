# Bulls and Cows Game ####
import random
random_number = str(random.randint(1000,9999))
guess = 0
guess_count = 0
cows = 0
bulls = 0
while int(guess) != random_number:
    print ("Cows:",cows, " Bulls:",bulls, " Guesses:",guess_count)
    x = 1
    cows = 0
    bulls = 0
    guess = input("Guess the number: ")
    if int(guess) == int(random_number):
        print ("You got it right! It was",guess)
        break
    if guess.isnumeric() == False:
        guess = input("Please enter a 4 digit number: ")
    while x < 5:
        if guess[x-1:x] == random_number[x-1:x]:
            cows += 1
            x += 1
        else:
            x += 1
            bulls += 1
    guess_count += 1
