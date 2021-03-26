from threading import Thread


class MyThread(Thread):
    def __init__(self, no) -> None:
        super().__init__()
        self.no = no

    def run(self) -> None:
        i = 1
        while i <= 10:
            print(f"{self.no} * {i} = {self.no * i}")
            i += 1


# Application

thread1 = MyThread(no=3)
thread2 = MyThread(no=5)
thread3 = MyThread(no=7)

thread1.start()
thread2.start()
thread3.start()
