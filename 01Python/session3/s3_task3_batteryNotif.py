'''
Session 5
Task 2:
    Notify your battery percentage
'''

import platform
import psutil

# Get current battery percentage
battery = psutil.sensors_battery()
percentage = battery.percent
print(percentage)

title = "Battery Status"
message =  "Your Battery is " + str(percentage) + "% Charged" 


if platform.system() == "Windows":
    # Code for Windows notification
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    toaster.show_toast(title, message)
    
elif platform.system() == "Linux":
    # Code for Linux notification
    import notify2
    notify2.init("Notification App")
    notf = notify2.Notification(title, message)
    notf.show()

# # Not working anymore dont know why
# from pynotify import Notfication
# Notfication("title","msg",duration=10).send()
    
######## ALTERNATIVE SOLUTION #########
'''
#from pynotifier import Notification
import psutil
from plyer import notification

cpu_freq=psutil.cpu_freq()  #current cpu frequency

notification.notify(
    #notification heading
    title = "CPU frequency",
    #notification body
    message="CPU frequency is: "+str(round(cpu_freq.current,3))+" MHZ",
    
    # displaying time
    timeout=10
)

'''