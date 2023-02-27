# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


number = int(input('Введите трехзначное число: '))
first_number = number % 10
second_number = number % 100 // 10
third_number = number // 100

print('Сумма цифр числа: ', first_number + second_number + third_number)
