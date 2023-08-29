# MAIN THREAD
# interpreter -> byte code > vm > execute
# cpython

import threading
import time

counter = 0

# sleep
# keyboard.wait
# input 
# listen

#

def input_thread():
    global counter
    while True:
        user_input = input("Reset counter value: \n")
        new_value = int(user_input)
        with threading.Lock():
            counter = new_value

def print_thread():
    global counter
    while True:
        with threading.Lock():
            counter += 1
        print("Counter:", counter)
        time.sleep(0.5)

input_thread = threading.Thread(target=input_thread , name="input thread")
print_thread = threading.Thread(target=print_thread)

input_thread.start() # start execution
print_thread.start()

input_thread.join() # poll wait
print_thread.join()




print("Program terminated.")

