# (Parte 2) Threads - Executando processamentos em paralelo

from threading import Thread
from time import sleep

"""
def ItWillTakeTime(text, time):
    sleep(time)
    print(text)


t1 = Thread(target=ItWillTakeTime, args=('Hello Word 1!', 5))
t1.start()

t2 = Thread(target=ItWillTakeTime, args=('Hello Word 2!', 1))
t2.start()

t3 = Thread(target=ItWillTakeTime, args=('Hello Word 3!', 2))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
"""

def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 10))
t1.start()
t1.join()

print('Thread acabou! ')
