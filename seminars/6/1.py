# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы первого массива(в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

import random

list_one = int(input('Введите количество элементов первого списка: '))
list_two = int(input('Введите количество элементов второго списка: '))

my_list_one = [random.randint(0, 10) for _ in range(list_one)]
my_list_two = [random.randint(0, 10) for _ in range(list_two)]

print(my_list_one, my_list_two)

# my_list = [for i in my_list_one if i not in my_list_two] Далее print(my_list)
my_list = []
for i in my_list_one:
    if i not in my_list_two:
        my_list.append(i)
print(my_list)
