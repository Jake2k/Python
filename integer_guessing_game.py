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
