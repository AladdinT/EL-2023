'''
Session 3
Task 1:
    1-Make your module that contain favourite websites and have function 
    called Firefox take url and open website 
    2- then make main file and print menu of sites for user and let him choice
'''
# Update mymodule.mybrowser with browser path
import mymodule.mybrowser as mybrowser

#print all my favourite urls
mybrowser.printFav()

#get the desired url 
key = str(input('Choose your website : '))

#open url from mybrowser
mybrowser.openUrl(mybrowser.myFavURL[key])
