# Напишите программу, которая находит все различные цифры в символьной строке.
# Для решения используйте множество (цифры будут различные, и поиск во множестве намного быстрее, чем в списке).
# Подсказка: можно использовать вот такое сравнение '0'<=x<='9'
# Пример:
# Введите строку: ab1n32kz2
# Различные цифры строки: 123

text = set(input('Введите строку: '))
num_set = {x for x in text if '0' <= x <= '9'}
print(num_set)