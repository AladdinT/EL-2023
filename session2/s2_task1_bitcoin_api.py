'''
Session 2
Quick Task 1:
    b) Write code to find automatically bitcoin rate
'''

# pip install requests
import requests

my_response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

print(str( my_response.json()['bpi']['USD']['rate'] ) + " $")
print(str( my_response.json()['bpi']['EUR']['rate'] ) + " €")