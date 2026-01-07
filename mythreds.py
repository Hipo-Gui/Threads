# (Parte 1) Threads - Executando processamentos em paralelo

from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, text: str, time: int):
        self.text = text
        self.time = time

        super().__init__()

    def run(self):
        sleep(self.time)
        print(self.text)


t1 = MyThread('Thread 1', 5)
t1.start()

t2 = MyThread('Thread 2', 3)
t2.start()

t3 = MyThread('Thread 3', 2)
t3.start()

for i in range(20):
    print(i)
    sleep(1)