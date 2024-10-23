from threading import Thread, Lock
from random import randint
from time import sleep


class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            x = randint(50, 500)
            self.balance += x
            print(f'Пополнение: {x}. Баланс:{self.balance}.')
            sleep(0.001)

    def take(self):
        for i in range(100):
            x = randint(50, 500)
            print(f'Запрос на {x}.')
            if x <= self.balance:
                self.balance -= x
                print(f'Снятие: {x}. Баланс:{self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.acquire()
            sleep(0.001)


sber = Bank()

t1 = Thread(target=Bank.deposit, args=(sber,))
t2 = Thread(target=Bank.take, args=(sber,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'Итоговый баланс: {sber.balance}')
