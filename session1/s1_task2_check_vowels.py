'''
Session 2
Task 2:
    Write a Python program to test whether a passed letter is a vowel or not.
'''

vowel_tuple = ('a','e','o','u','i')

while True :
    x = str(input("Enter a letter : "))
    if x[0] in vowel_tuple :
        print(f'{x[-1]} is a vowel ')
    else:
        print(f'{x[-1]} is not a vowel ')
