import random
from datetime import datetime

food_list = []
price_list = []
bill_list = []
prices = []

def lets_go_shopping():
    total = 0
    list_len = 0
    print ("Shopping list - Tax Calculator")
    while list_len < 1 or list_len > 99:
        list_len = int(input("How many items are we buying today?  : "))
    # Creates random lists
    lines = open('food.txt').read().splitlines()
    while len(food_list) < list_len:
        food_list.append(random.choice(lines))
    while len(price_list) < list_len:
        price_list.append(round(random.uniform(1,25),2))
    # Zips the lists together
    bill_list = list(zip(food_list,price_list))
    total = shopping_list_graphic(bill_list)
    trust = input("Is this right? (y/n) :")
    if trust != "n":
        print ("\nWait, we need to add tax!")
    else:
        print ("Your right, we are missing something.")
    tax_calc(total,trust)
    
def shopping_list_graphic(bill_list): 
    list_width = 30
    total = 0
    print ("-" * list_width)
    print ("#        SHOPPING LIST       #")
    for item in bill_list:
        if len(str(item[1])) == 5:
            print ("#  ",item[0],(15 - len(item[0])) * " " ,item[1],"  #")
        if len(str(item[1])) == 4:
            print ("#  ",item[0],(16 - len(item[0])) * " " ,item[1],"  #")
        if len(str(item[1])) == 3:
            print ("#  ",item[0],(17 - len(item[0])) * " " ,item[1],"  #")
        if len(str(item[1])) == 2:
            print ("#  ",item[0],(18 - len(item[0])) * " " ,item[1],"  #")
    for item in bill_list:
        total += item[1]
    total = "{:.2f}".format(total)
    if float(total) < 100:
        print ("#   Total    :::    ", total,"  #")
    else:
        print ("#   Total    :::   ", total,"  #")
    print ("-" * list_width)
    return total


def tax_calc(total,trust):
    if trust == "n":
        print ("The normal tax rate is 20%, but since your honest have 5% off")
        new_total = "{:.2f}".format(float(total) * float(1.15))
        print (f"Your final total comes to £{new_total}")   
    else:
        print ("Since I can't trust you to tell me the right tax rate, we shall let fate decide.")
        now = datetime.now()
        hours = now.strftime("%H")
        minutes = input(f"What is the minute time? {hours} : ")
        now = datetime.now()
        actual_minutes = now.strftime("%M")
        if minutes == actual_minutes:
            new_total = "{:.2f}".format(float(total) * float(1.25))
            print ("Thank you for being honest, the rate is 20%.")
            print (f"Your final total comes to £{new_total}")              
        else:
            print ("You just couldn't help yourself could you!")
            print ("50% TAX")
            new_total = "{:.2f}".format(float(total) * float(1.5))
            print (f"Your final total comes to £{new_total}")    
lets_go_shopping()
