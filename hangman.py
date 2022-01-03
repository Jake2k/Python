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
