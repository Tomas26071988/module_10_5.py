from multiprocessing import Pool
from datetime import datetime


#   Создал декоратор для подсчета времени (секундомер)
def decorator(func):
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()
        print(end - start)

    return wrapper


#   Основная функция по заданию
def read_info(name):
    all_data = []  # Создается огромнейший список со всеми строками из файлов
    with open(name, 'r') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]
# ['./file 1.txt', './file 2.txt', './file 3.txt', './file 4.txt']


@decorator
def all_data_line_call():  # Создал функцию для линейного вызова + декоратор для подсчета времени
    for file in filenames:
        read_info(file)


@decorator
def all_data_multi_process():  # Создал функцию для многопроцессорного вызова + декоратор для подсчета времени
    with Pool() as process:
        process.map(read_info, filenames)


if __name__ == '__main__':  # Вызывать функции по очереди
    all_data_line_call()
    # all_data_multi_process()

# Для функции линейного вызова all_data_line_call() время выполнения: 0:00:03.255826
# Для функции многопроцессорного вызова all_data_multi_process() время выполнения: 0:00:03.242332