### List numbers < 5 filter ###
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def list_less_than_5(list1):
    less_than_5_list = [1]
    for number in list1:
        if number < 5:
            less_than_5_list.append(number)
    return less_than_5_list
print (list_less_than_5(list1))
