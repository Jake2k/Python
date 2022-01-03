count_dict = {}

with open("nameslist.txt", "r") as file:
    name = file.readline()
    while name:
        name = name.strip()
        if name in count_dict:
            count_dict[name] +=1
        else:
            count_dict[name] = 1
        name = file.readline()
print (count_dict)
