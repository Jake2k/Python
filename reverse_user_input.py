# Backwards Input ###
user_string = input("Please enter a sentence: ")
def sentence_backwards(user_string):
    string = user_string.split()
    new_sentence = []
    for word in string:
        new_sentence.insert(0,word)
    return new_sentence
print (sentence_backwards(user_string))

