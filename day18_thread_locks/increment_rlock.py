import threading

x = 0


def increment():
    global x
    x += 1


def task(lock: threading.RLock):
    print("Entering thread:", threading.current_thread().getName())
    for _ in range(100000):
        lock.acquire()
        increment()
    for _ in range(100000):
        lock.release()


def main_task():
    global x
    x = 0
    lock = threading.RLock()
    t1 = threading.Thread(target=task, args=(lock,))
    t2 = threading.Thread(target=task, args=(lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


for i in range(10):
    main_task()
    print(f"Iteration {i} ----> {x}")
