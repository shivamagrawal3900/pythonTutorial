from threading import Timer


def say(name):
    for i in range(10):
        print(name)


t = Timer(5, say, args=("Bodacious IT Hub",))
t.start()
