'''
Session 1
Task 1:
    Write a Python program to count the number 4 in a given list.
'''

given_list = str(input("enter a string of numbers : "))
given_list = list(given_list)
counter = given_list.count('4')

print(f"There are {counter} of 4's in this list ")
