# First and last ###
import random
list_a = []
while len(list_a) < 50:
    random_number = random.randint(1,100)
    list_a.append(random_number)
list_b = [list_a[0], list_a[-1]]
print (list_b)
