import time
from time import sleep
from threading import Thread


# word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")



started_at = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
ended_at = time.time()
elapsed = ended_at - started_at
print(f'Функция работала {elapsed} секунд(ы)')



started_at = time.time()
wr_w1 = Thread(target = write_words, args = (10, 'example5.txt'))
wr_w2 = Thread(target = write_words, args = (30, 'example6.txt'))
wr_w3 = Thread(target = write_words, args = (200, 'example7.txt'))
wr_w4 = Thread(target = write_words, args = (100, 'example8.txt'))
wr_w1.start()
wr_w2.start()
wr_w3.start()
wr_w4.start()

wr_w1.join()
wr_w2.join()
wr_w3.join()
wr_w4.join()
ended_at = time.time()
elapsed = ended_at - started_at
print(f'Функция работала {elapsed} секунд(ы)')







