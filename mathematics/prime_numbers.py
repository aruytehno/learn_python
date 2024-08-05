'''
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
https://ru.wikipedia.org/wiki/Простое_число
https://en.wikipedia.org/wiki/List_of_prime_numbers
https://habr.com/ru/articles/122538/

Используются списковые включения (list comprehension)
'''

prime_numbers_list_1 = [2, 3, 5, 7]
for i in range(2, 100):
    if not i % 2 == 0:
        if not i % 3 == 0:
            if not i % 5 == 0:
                if not i % 7 == 0:
                    prime_numbers_list_1.append(i)
print(prime_numbers_list_1)

prime_numbers_list_2 = [2, 3, 5, 7]
for n in range(2, 100):
    if all(not n % i == 0 for i in [2, 3, 5, 7]):
        prime_numbers_list_2.append(n)
print(prime_numbers_list_2)

# list comprehension
print([2, 3, 5, 7] + [x for x in range(2, 100) if not x % 2 == 0 if not x % 3 == 0 if not x % 5 == 0 if not x % 7 == 0])
# short
print([2, 3, 5, 7] + [x for x in range(2, 100) if all(not x % i == 0 for i in [2, 3, 5, 7])])

