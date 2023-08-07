
import webbrowser

# Replace with your browser path
browser_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'


myFavURL = {
    'fb' : 'facbook.com' ,
    'yt' : 'youtube.com' ,
    'insta' : 'instagram.com',
    'udacity' : 'https://classroom.udacity.com/',
    'calendar' : 'calendar.google.com'
}

def openUrl (url):
    webbrowser.get(browser_path).open(url)

def printFav ():
    for key in myFavURL:
        print(key , end= "\t")
    print(end="\n")
