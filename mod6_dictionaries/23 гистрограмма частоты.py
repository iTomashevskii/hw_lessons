# Лингвистам нужно собрать данные о частоте букв в тексте, исходя из этих данных будет строиться гистограмма частоты букв.
# Напишите программу, которая получает сам текст и считает, сколько раз в строке встречается каждый символ.
# На экран нужно вывести содержимое в виде таблицы, отсортированное по алфавиту, а также максимальное значение частоты.
# Пример:
# Введите текст: Здесь что-то написано
#   : 2   - : 1   З : 1   а : 2   д : 1   е : 1   и : 1   н : 2   о : 3   п : 1   с : 2   т : 2   ч : 1   ь : 1
# Максимальная частота: 3
#
def sorted_histogram(string):
	hist = {}
	for sym in sorted(string):
		hist[sym] = string.count(sym)
	return hist


text = input('Введите текст: ')
for _ in sorted_histogram(text):
	print(f'{_}: {sorted_histogram(text)[_]}')
print('Максимальная частота:', max(sorted_histogram(text).values()))

# из решения
# text = input("Введите текст: ")
# frequency = {}
# for symbol in text:
#     if symbol in frequency:
#         frequency[symbol] += 1
#     else:
#         frequency[symbol] = 1
# for letter, freq in frequency.items():
#     print(letter, ':', freq)
# print("Максимальная частота: ", max(frequency.values()))


