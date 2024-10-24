import time
from threading import Thread
from random import randint
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.quest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))


class Cafe:
    list_quest = []

    def __init__(self, *table):
        self.queue = queue.Queue()
        self.tables = list(table)

    def guest_arrival(self, *guest):
        len_guests = len(list(guest))
        guests_tables = min(len_guests, len(self.tables))
        for i in range(guests_tables):
            self.tables[i].guest = guest[i]
            set_thr = guest[i]
            set_thr.start()
            Cafe.list_quest.append(set_thr)
            print(f'{list(guest)[i].name} сел(-а) за стол номер {self.tables[i].number}')
        if len_guests > guests_tables:
            for q in range(guests_tables, len_guests):
                self.queue.put(guest[q])
                print(f'{list(guest)[q].name} в очереди')

    def discuss_guests(self):
        while not (self.queue.empty()) or Cafe.check_table(self):
            for table in self.tables:
                if not (table.guest is None) and not (table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not (self.queue.empty()) and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер '
                          f'{table.number}')
                    set_thr = table.guest
                    set_thr.start()
                    Cafe.list_quest.append(set_thr)

    def check_table(self):
        for table in self.tables:
            if table.guest is not None:
                return True
        return False



tables = [Table(number) for number in range(1, 6)]

guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria',
                'Nikita', 'Galina', 'Pavel', 'Ilya','Alexandra', 'Эдуард']

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_guests()
