# (Parte 3) Threads - Executando processamentos em paralelo

from threading import Lock, Thread
from time import sleep

class ticket:
    """
    Classe que vende ingresso
    """

    def __init__(self, stock: int):
        """ Inicializando...

        :param estoque: quantidade de ingressos em estoque
        """

        self.stock = stock
        # Nosso cadeado 
        self.lock = Lock()

    def buy(self, amount: int):
        """
        Compra determinada quantidade de ingressos

        :param quatidade: A quantidade de ingresso que deseja comprar
        :type quantidade: int
        :rtype: None
        """
        #Tranca o método
        self.lock.acquire()

        if self.stock < amount:
            print("We don't have enough tickets. " )
            # Libera o método 
            self.lock.release()
            return
        
        sleep(1)

        self.stock -= amount
        print(f'You bought {amount} ticket(s).'
              f'We still have{self.stock} in stock.')
        
        #Libera o método 
        self.lock.release()

if __name__ == '__main__':
    ticket = ticket(10)

    for i in range(20):
        t = Thread(target=ticket.buy, args=(i,))
        t.start()

    print(ticket.stock)

