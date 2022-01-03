# Word is palindrome ? ###
word = input("Enter a palindrome: ")
if word == word[::-1]:
    print ("Word is a palinedrome")
else:
    print ("Word is not a palinedrome")
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = []
for num in a:
    if (num % 2) == 0:
        new_list.append(num)
print (new_list)
