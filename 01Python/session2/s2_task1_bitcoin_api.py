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



###################################
# there is another way that is out of scope but fun
# using web scraping 
# pip install requests lxml beautifulsoup4
import requests
from bs4 import BeautifulSoup

my_response = requests.get("https://www.coindesk.com/price/bitcoin")

src_code = my_response.content
soup = BeautifulSoup(src_code , "lxml")

price_span = soup.find("span",{"class":"currency-pricestyles__Price-sc-1rux8hj-0 eEpEzP"})
currency_span = soup.find("span",{"class":"currency-pricestyles__Symbol-sc-1rux8hj-1 iiVBBR"})

print(price_span.text + ' ' + currency_span.text)
