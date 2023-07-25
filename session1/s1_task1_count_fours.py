'''
Session 2
Task 1:
    Write a Python program to count the number 4 in a given list.
'''

given_list = str(input("enter a string of numbers : "))
given_list = list(given_list)
counter = 0
for i in range(len(given_list)):
    if given_list[i] == '4':
        counter+=1

print(f"There are {counter} of 4's in this list ")