# Fib sequence ###
amount_of_num = input("How many fibonnaci numbers to generate? ")
def fib_stuff(amount_of_num):
    count = 0
    n1, n2 = 1, 1
    new_list = []
    while count < int(amount_of_num):
        new_list.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    return new_list
print (fib_stuff(amount_of_num))
