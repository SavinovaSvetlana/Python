# Функция фильтр

data = [13, 15, 98, 175, 5, 45]
print(data)
res = list(filter(lambda x: x % 10 == 5, data))
print(res)


# Функция зип
users = ['user1', 'user2', 'user3']
ids = [3, 8, 56]
data = list(zip(users, ids))
print(data)


# Функция енумерайт
users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)
