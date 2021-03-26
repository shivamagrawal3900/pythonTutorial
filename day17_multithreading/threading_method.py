from threading import Thread


def table(no):
    for i in range(10):
        print(f"{no} * {i + 1} = {no * (i + 1)}")


thread1 = Thread(target=table, args=(3,))
thread2 = Thread(target=table, args=(5,))
thread3 = Thread(target=table, args=(7,))

# OR below foramt
# thread1 = Thread(target=table(3))
# thread2 = Thread(target=table(5))
# thread3 = Thread(target=table(7))

thread1.start()
thread2.start()
thread3.start()
