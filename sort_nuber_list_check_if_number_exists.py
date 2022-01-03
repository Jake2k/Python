# is number in the list? ####
import random
number = random.randint(1,25)
number_list = []
def is_in_list(number_list):
    while len(sorted(number_list)) < 20:
        number_list.append(random.randint(1,50))
    number_list.sort()
    for integer in number_list:
        if integer == number:
            return True
    return False
print (is_in_list(number_list))
