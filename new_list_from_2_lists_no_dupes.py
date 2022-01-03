# New list - No dupes 
import random
list_a =[]
while len(list_a) < 25:
    list_a.append(random.randint(1,10))
print (list_a)
def no_dupes(list_a):
    list_b = []
    for num in list_a:
            if num not in list_b:
                list_b.append(num)
    return list_b
print (no_dupes(list_a))
