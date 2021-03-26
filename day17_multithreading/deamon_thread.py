import time
from threading import Thread


class DaemonThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        for i in range(10):
            print("I am daemon thread!")
            time.sleep(2)


# Application
t1 = DaemonThread()
t1.setDaemon(True)
t1.start()
print("byee")
