# Задача 2. Олимпиада
# В олимпиаде по программированию участвует N человек, в списке участников они обозначаются под
# номерами 1, 2, 3, 4 и так далее до N. Эти участники поделены на команды по K человек.
# Напишите программу, которая принимает на вход количество участников и количество человек в каждой команде,
# затем генерирует список таких команд и выводит его на экран.
# Обеспечьте контроль ввода: в каждой команде должно быть ровно по K человек.
#
# Пример 1:
# Кол-во участников: 12
# Кол-во человек в команде: 4
# Общий список команд: [[1, 2 ,3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#
# Пример 2:
# Кол-во участников: 12
# Кол-во человек в команде: 5
# 12 участников невозможно поделить на команды по 5 человек!
#

N_participants = int(input('Кол-во участников: '))
team_size = int(input('Кол-во человек в команде: '))
team_list = []
N = team_size + 1

if N_participants % team_size != 0:
	print(f'{N_participants} участников невозможно поделить на команды по {team_size} человек!')
else:
	for team in range(N_participants // team_size):
		team = list(range(N - team_size, N))
		team_list.append(team)
		N += team_size

	print('Общий список команд:', team_list)