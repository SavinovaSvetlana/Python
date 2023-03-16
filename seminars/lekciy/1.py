# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]


import random

my_list = int(input('Введите количество элементов первого списка: '))
my_list_one = [random.randint(0, 10) for _ in range(my_list)]
print(my_list_one)
# temp_list = []

# for i in my_list_one:
#     if i % 2 == 0:
#         temp_list.append((i, i ** 2))


# print(temp_list)

res = map(int, my_list_one)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
