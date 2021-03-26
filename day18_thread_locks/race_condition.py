import threading

x = 0


def increment():
    global x
    x += 1


def task():
    for _ in range(100000):
        increment()


def main_task():
    global x
    x = 0
    t1 = threading.Thread(target=task)
    t2 = threading.Thread(target=task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


for i in range(10):
    main_task()
    print(f"Iteration {i} ----> {x}")
