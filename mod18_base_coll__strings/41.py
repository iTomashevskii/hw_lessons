# Задача 1. Шифр Цезаря 2
# Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря.
# Напомним, что в таком способе шифрования каждая буква заменяется на следующую по алфавиту через K позиций по кругу.
# Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования.
# Не используйте конкатенацию и сделайте так, чтобы текст был в одном регистре.

def caesar(word, shift):
	# new_sym = ''
	# for i_letter in range(len(alfabet)):
	# 	if sym == alfabet[i_letter] and i_letter + shift < len(alfabet):
	# 		new_sym = alfabet[i_letter + shift]
	# 	elif sym == alfabet[i_letter] and i_letter + shift >= len(alfabet):
	# 		new_sym = alfabet[i_letter + shift - len(alfabet)]
	# if new_sym == '':
	# 	new_sym = sym
	# return new_sym

	char_list = [(alphabet[(alphabet.index(symbol) + shift) % 33] if symbol in alphabet else symbol) for symbol in word]
	# new_str = ''
	# for i_char in char_list:
	# 	new_str += i_char
	new_str = ''.join(char_list)
	return new_str

alphabet = ("а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я").split()
message = input('Введите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))

#cipher = [caesar(sym, shift) for sym in message]
cipher = caesar(message, shift)
print('Зашифрованное сообщение:', cipher)
# for sym in cipher:
# 	print(sym, end='')
