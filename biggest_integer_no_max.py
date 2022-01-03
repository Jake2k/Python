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
