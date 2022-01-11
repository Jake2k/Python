from word2number import w2n
from number2words import Number2Words

def magic(number):
  while number != 4:
    number2words = Number2Words(number).convert()
    length = len(number2words) - number2words.count(" ") - 4
    print (f"{number} is {length}")
    number = length
  return (f"{number} is magic.")
    
print (magic(59405437))
