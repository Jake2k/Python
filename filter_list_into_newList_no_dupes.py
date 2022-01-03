# List Filter non same ###
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def print_common(list_A,list_B):
    list_C = []
    for num in list_A:
        if num in list_B:
            if num != list_C:
                list_C.append(num)
    return list_C
print (print_common(a,b))
