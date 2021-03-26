import threading
from threading import Thread


def table(no):
    print(threading.current_thread().getName())
    print(threading.main_thread().getName())
    for i in range(10):
        print(f"{no} * {i + 1} = {no * (i + 1)}")


thread1 = Thread(target=table, args=(3,))
thread2 = Thread(target=table, args=(5,))
thread3 = Thread(target=table, args=(7,))

thread1.setName("one")
thread2.setName("two")
thread3.setName("three")

thread1.start()
thread2.start()
thread3.start()

print(thread1.is_alive())
print(thread2.is_alive())
print(thread3.is_alive())

print([t.getName() for t in threading.enumerate()])
print(threading.current_thread())

print(thread1.getName())
print(thread2.getName())
print(thread3.getName())

print("Print before joining threads!!")

thread1.join()
thread2.join()
thread3.join()

print("Printing after joining the threads. This should come at the end.")
