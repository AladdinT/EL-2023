'''
Session 1
Task 3:
    Print the calendar of a given month and year
'''

import calendar as cal
year = int( input("Year : ") )
month = int( input("Month : ") )
print("\n" + cal.month(year,month))