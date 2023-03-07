# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

numbers_1 = int(input('Введите количество элементов в списке 1: '))
numbers_2 = int(input('Введите количество элементов в списке 2: '))

list_1 = [random.randint(1, 20) for _ in range(numbers_1)]
list_2 = [random.randint(1, 20) for _ in range(numbers_2)]

print(list_1, list_2)

plenty = set(list_1) | set(list_2)
print(sorted(plenty))