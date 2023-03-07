# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

my_offer = '''Сшит колпак, вязан колпак, да не по-колпаковски. 
            Вылит колокол, кован колокол, да не по-колоколовски. 
            Надо колпак переколпаковать, да перевыколпаковать. 
            Надо колокол переколоколовать, да перевыколоколовать.'''

my_list = my_offer.lower().split()
print(len(set(my_list)))


catalog = {}


for word in my_list:
    catalog[word] = catalog.get(word, 0) + 1
count = 0
for _ in catalog:
    count += 1
print(count)


key = catalog.keys()
print(len(key))
