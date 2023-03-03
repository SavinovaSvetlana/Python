# Задача №19. Решение в группах дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

N = int(input('Введите N'))
K = int(input('Введите K'))
my_list = [i for i in range(N)]
print(my_list)
list_one = my_list[:K]
list_two = my_list[K:]
my_list_end = list_two + list_one
print(my_list_end)


# my_list = [i for i in range(10)]  # my_list =[i**2 for i in range(10) if ]
# print(my_list)
# shift = int(input('Введите сдвиг: '))
# for i in range(shift):
#     my_list.insert(0, my_list.pop(-1))
# print(my_list)
