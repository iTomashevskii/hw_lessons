# Задача 3. Удаление части
# На вход в программу подаётся строка, состоящая из прописных и заглавных букв кириллицы.
# Напишите код, который проверяет, каких букв в строке больше, прописных или заглавных.
# Если заглавных букв больше, то сделать все буквы строки заглавными, иначе сделать все прописными.
# Подсказка: используйте методы islower() и/или isupper().
#
# Пример:
# Введите строку: ПитоН - этО хорошО
# Результат: питон - это хорошо
#
# Пример 2:
# Введите строку: ПиТоН - ЭтО УДоБнО
# Результат: ПИТОН - ЭТО УДОБНО

message = input('Введите сообщение: ')
# count = 0
# for letter in message:
# 	if letter.isupper() == True:
# 		count += 1
# 	else:
# 		count -= 1
# if count >= 0:
# 	print(message.upper())
# else:
# 	print(message.lower())

lowers = len([letter for letter in message if letter.islower()])
uppers = len([letter for letter in message if letter.isupper()])

if lowers > uppers:
    print("Результат:", message.lower())
else:
    print("Результат:", message.upper())


