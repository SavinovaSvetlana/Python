# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

len_list = int(input('Введите количество элементов списка: '))
my_list = [random.randint(0, 10) for _ in range(len_list)]
max_number = int(input('Введите максимальный диапозон: '))
min_number = int(input('Введите минимальный диапозон: '))
print(my_list)

temp_list = []
for i in range(len(my_list)):
    if min_number <= my_list[i] <= max_number:
        # print(i)
        temp_list.append(i)
print(temp_list)
