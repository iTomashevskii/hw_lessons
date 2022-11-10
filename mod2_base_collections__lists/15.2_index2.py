#Задача 2. Кратность
#Пользователь вводит список из N чисел и число K. Напишите код,
# выводящий на экран сумму индексов элементов списка, которые кратны K.

nums_list = []
new_nums_list = []
N = int(input('Кол-во чисел в списке: '))
for _ in range(N):
	num = int(input(f'Введите {_ + 1} число: '))
	nums_list.append(num)
K = int(input('Введите делитель: '))
sum = 0
for _ in nums_list:
	if _ % K == 0:
		sum += _
		new_nums_list.append(_)
print(f'Cумма индексов элементов списка, которые кратны K {new_nums_list}:', sum)