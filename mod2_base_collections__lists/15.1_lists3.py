#В любой компании есть список сотрудников. Руководство одной компании хочет знать,
# на рабочем месте ли сейчас сотрудник. У каждого сотрудника есть пропуск со своим ID-номером
# (это положительное число), список активных пропусков сотрудников известен заранее.
# Напишите программу, которая сначала запрашивает у пользователя количество сотрудников в офисе,
# ID их пропусков, а затем запрашивает ID пропуска, который нужно найти в этом списке.
# Если такой есть, то вывести «Сотрудник на месте», а иначе «Сотрудник не работает!».
#https://go.skillbox.ru/profession/profession-python/python-basic/8bb5d61c-6dae-4442-a235-3eb155342940/videolesson

employee_num = int(input('Кол-во сотрудников в офисе: '))
employees = []
check = 0
for _ in range(employee_num):
	employee_id = int(input('ID сотрудника: '))
	employees.append(employee_id)
employee_search = int(input('Какой ID ищем? '))
for _ in employees:
	if _ == employee_search:
		check += 1
		print('Cотрудник на месте')
if check == 0:
	print('Сотрудник не работает!')