# Задача 3. Улучшенная лингвистика
# Мы уже писали программу для лингвистов, которая считала количество определённых букв в тексте.
# Теперь эту программу нужно улучшить. Есть список из трёх слов, которые вводит пользователь.
# Затем вводится сам текст произведения строго по словам. Текст вводится до тех пор, пока не встретится слово end.
# Напишите программу, которая посчитает, сколько раз слова пользователя встречаются в тексте.
#
# Пример:
# Введите 1 слово: я
# Введите 2 слово: год
# Введите 3 слово: лучший
# Слово из текста: этот
# Слово из текста: год
# Слово из текста: -
# Слово из текста: лучший
# Слово из текста: год
# Подсчёт слов в тексте
# я: 0
# год: 2
# лучший: 1
#
word_list = []
counts = [0, 0, 0]
for _ in range(3):
	word = input(f'Введите {_ + 1} слово: ')
	word_list.append(word)

text = input('Слово из текста: ')
while text != 'end':
	for i in range(3):
		if word_list[i] == text:
			counts[i] += 1
	text = input('Слово из текста: ')

# print(f'Подсчёт слов в тексте\n'
#       f'{word_list[0]}: {counts[0]}\n'
#       f'{word_list[1]}: {counts[1]}\n'
#       f'{word_list[2]}: {counts[2]}\n')
print('\nПодсчёт слов в тексте:')
for _ in range(3):
	print(f'{word_list[_]}: {counts[_]}')
