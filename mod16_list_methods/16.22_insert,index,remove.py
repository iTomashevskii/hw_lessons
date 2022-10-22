# Задача 2. Сокращения
# В одной компании наступили «тёмные времена», и сотрудников стали сокращать. Зарплаты сотрудников хранятся в списке из N этих самых зарплат.
# Зарплаты уже уволенных сотрудников обозначаются в списке числом 0.
# Напишите программу, которая запрашивает у пользователя количество сотрудников и их зарплаты, # затем удаляет все элементы списка
# со значением 0 и выводит в консоль, сколько сотрудников осталось, а также их зарплаты. # Дополнительный список использовать нельзя.
#
# Пример:
# Кол-во сотрудников: 7
# Зарплата 1 сотрудника: 10000  # Зарплата 2 сотрудника: 25000  # Зарплата 3 сотрудника: 0  # Зарплата 4 сотрудника: 50000
# Зарплата 5 сотрудника: 60000  # Зарплата 6 сотрудника: 0  # Зарплата 7 сотрудника: 17000
# Осталось сотрудников: 5
# Зарплаты: [10000, 25000, 50000, 60000, 17000]
#
# Дополнительно: выведите на экран максимальную и минимальную зарплату оставшихся сотрудников.
# Для этого используйте функции max и min. Да, те самые, которыми нельзя называть переменные. В скобках функций просто укажите список.

N = int(input('Кол-во сотрудников: '))
salarys = []
for _ in range(N):
	wage = int(input(f'Зарплата {_ + 1} сотрудника: '))
	salarys.append(wage)
for wage in salarys:
	if wage == 0:
		salarys.remove(0)
print(f'\nОсталось сотрудников: {len(salarys)}\nЗарплаты: {salarys}\nМинимальная ЗП: {min(salarys)}\nМаксимальная ЗП: {max(salarys)}')