# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
import random
# lengh_mass = int(input('Ведите количество оценок: '))
# random_mass = [random.randint(1, 5) for _ in range(lengh_mass)]
# print(random_mass)
# i = 0
# while i < len(random_mass):
#     if random_mass[i] == 4:  # or random_mass[i] == 5:
#         random_mass[i] == 1
#     i += 1
# print(random_mass)


numbers = [random.randint(1, 5) for _ in range(6)]
print(numbers)

max_count = max(numbers)
min_count = min(numbers)
print(f'Максимальная оценка {max_count}, минимальная оценка {min_count}')
for i in range(len(numbers)):
    if numbers[i] == max_count:
        numbers[i] = min_count
print(numbers)
