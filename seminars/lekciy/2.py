# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?


data = '23 56 4 13 89 54 31'
print(data)

data = list(map(int, data.split()))
print(data)