# Random lists into 1 list no dupes ####
import random
list_a = []
list_b = []
while len(list_a) < 25:
    random_int = random.randint(1,50)
    list_a.append(random_int)
while len(list_b) < 25:
    random_int = random.randint(1,50)
    list_b.append(random_int)
def list_compare(a,b):
    list_c = []
    for number in list_a:
        if number in list_b:
            if number != list_c:
                list_c.append(number)
    return list_c
print ("List A:",list_a)
print ("List B:",list_b)
print ("List C:",list_compare(list_a,list_b))
