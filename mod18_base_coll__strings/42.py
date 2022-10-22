# Задача 2. Путь к файлу
# Все данные сайта лежат в одном проекте. При написании кода, внутри этого проекта часто
# используются абсолютные пути файлов, которые необходимо проверять.
# Пользователь вводит абсолютный путь к текстовому файлу, а также проверяемые данные: диск и расширение файла.
# Напишите программу, которая проверяет корректность этого пути.
#
# Пример:
# Путь к файлу: C:/user/docs/folder/new_file.txt
# На каком диске должен лежать файл: C
# Требуемое расширение файла: .txt
# Путь корректен!

path = input('Путь к файлу: ')
disk = input('На каком диске должен лежать файл: ')
extension = input('Требуемое расширение файла: ')

if not path.startswith(disk):
	print('Не тот диск')
elif not path.endswith(extension):
	print('Не то расширение')
else:
	print('Путь корректен!')
