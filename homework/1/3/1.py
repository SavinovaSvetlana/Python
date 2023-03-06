# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100. Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

list_1 = [random.randint(1, 100) for _ in range(20)]
value = int(input('Введите число от 1 до 100: '))
print(list_1)

found = list_1[0]
for item in list_1:
    if abs(item - value) < abs(found - value):
        found = item

print(f'Число {value} встречается {list_1.count(value)}')
print(f'Ближайшее число {(found)}')
