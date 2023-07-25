'''
Session 2
Task 3:
    Write a python program to access environment variables.
'''

import os

print()
#Prints all system variables
for k, v in os.environ.items():
    print(f'{k}',end=', ')
print('\n')

#gets variables' values
while 1:
    get_value = str(input('Get : '))
    print(os.environ.get(get_value) )


