'''
Session 3
Task2:
    1-Write a code to suggest automatically activities for you 
    2-Get your public IP
'''
#################### Write a code to suggest automatically activities for you #################
import requests
from mymodule.mybrowser import openUrl
url = requests.get("http://www.boredapi.com/api/activity")

print("-"*30)
print('Categoty : ' + url.json()['type'])
print('Activity : ' + url.json()['activity'])
if ( str(url.json()['link']) != ""):
    print('Link : ' + url.json()['link'])
    if( str(input("Open Url ? (y/n) :  " )) == "y"):
        openUrl(str(url.json()['link']))

print("-"*30)

######################### Get your public IP #################################################

# local
import socket   
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   
print("Local IP Address  : " + IPAddr )

# public
url = requests.get("https://api.ipify.org/?format=json")

print("Public IP Address : " + str(url.json()['ip']) )
print("-"*30)


##############################################################################################
