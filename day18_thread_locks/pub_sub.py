import threading
import time

x = None


def print_x():
    global x
    for _ in range(10):
        while not x:
            time.sleep(2)
        else:
            print("Value of x = ", x)
            x = None


def set_x():
    global x
    for i in range(1, 11):
        while x:
            time.sleep(2)
        else:
            print("setting value of x to", i)
            x = i


pub_thread = threading.Thread(target=set_x)
sub_thread = threading.Thread(target=print_x)

pub_thread.start()
sub_thread.start()
