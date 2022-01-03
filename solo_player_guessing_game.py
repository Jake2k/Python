# Guessing game one
import random

random_int = random.randint(1,9)
guess = 0
guess_count = 0

while guess != random_int:
    if int(guess_count) != 0:
        print ("Guesses:",guess_count)
    if int(guess) == 0:
        guess = input("Guess the number between 1 and 9: ")
    elif int(guess) == random_int:
        print ("You guessed correct, it was", guess,"!")
        break
    elif int(guess) > random_int:
        print ("You guessed to high, guess again")
        guess = input("Guess the number between 1 and 9: ")
        guess_count += 1
    elif int(guess) < random_int:
        print ("You guessed to low, guess again")
        guess_count += 1
        guess = input("Guess the number between 1 and 9: ")
