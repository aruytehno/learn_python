import collections

'''
Скрипт для нахождения чисел вампиров до 100
https://ru.wikipedia.org/wiki/Число-вампир
https://en.wikipedia.org/wiki/Vampire_number

Используются списковые включения (list comprehension)
'''
for i in range(10, 100):
    for n in range(i, 100):
        list1 = [int(x) for x in str(i)] + [int(x) for x in str(n)]
        list2 = [int(x) for x in str(i * n)]
        if collections.Counter(list1) == collections.Counter(list2):
            print(str(i * n) + ' = ' + str(i) + ' x ' + str(n))
