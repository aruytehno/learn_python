from itertools import chain
import random
import string

'''
Генератор паролей на списковых включениях в одну строку
'''

print(''.join(str(x) for x in [chr(random.choice(list(chain(range(65, 91), range(97, 123), range(48, 58))))) for x in range(20)]))
# short
print(''.join(str(x) for x in [random.choice(string.ascii_letters + string.digits) for x in range(20)]))
