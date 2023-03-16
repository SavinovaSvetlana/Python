# Функция фильтр

data = [13, 15, 98, 175, 5, 45]
print(data)
res = list(filter(lambda x: x % 10 == 5, data))
print(res)
