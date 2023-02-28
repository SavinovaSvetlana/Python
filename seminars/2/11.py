# Задача №11. Решение в группах. Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6


# a = 5
# b = 10
# print(a, b)

# a, b = b, a
# print(a, b)

# меняем значение переменных


fibo_1 = 0
fibo_2 = 1
fibo_cur = 0
count = 1
number = int(input('Введите передел: '))

while fibo_cur < number:
    fibo_cur = fibo_1 + fibo_2
    fibo_1, fibo_2 = fibo_2, fibo_cur
    count += 1
print(count if number == fibo_cur else '-1')
