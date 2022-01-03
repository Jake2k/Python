# Prime number check ###
number = input("Enter a number: ")
def is_number_prime(number):    
    list_a = [*range(2,number - 1,1)]
    for num in list_a:
        if number % num == 0:
            print ("Number is not prime")
            return number
            break
        else:
            print ("Number is prime")
            return number
print (is_number_prime(int(number)))
