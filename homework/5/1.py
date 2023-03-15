# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


import random

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))


# def degree_number(a, b):
#     print(number_1**number_2)
# degree_number(number_1, number_2)


# def degree_number(a, b):
#     return number_1**number_2


# print(degree_number(number_1, number_2))


def degree_number(a, b):
    if b == 1:
        return a
    else:
        return a**b


print(degree_number(number_1, number_2))
