# List divisor of numbers ###
number = int(input("Enter a number: "))
divisor_list = []
list_range = list(range(1,number+1))
for integer in list_range:
    if (number % integer) == 0:
        divisor_list.append(integer)    
print (divisor_list)
