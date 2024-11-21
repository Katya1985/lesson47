import threading
import time

class Knight(threading.Thread):


    def __init__(self, name: str, power: int):  # имя рыцаря, сила рыцаря
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def run(self):
        count_day = 0
        warrior = 100
        print(f"{self.name}, на нас напали!")
        while warrior > 0:
            warrior -= self.power
            count_day += 1
            time.sleep(1)



            print(f"{self.name} сражается {count_day} день(дня), осталось {warrior} воинов.")
        else:
            print(f"{self.name} одержал победу спустя {count_day} дней(дня)!")



if __name__ == '__main__':
# Создание класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
print('Все битвы закончились!')

# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения
