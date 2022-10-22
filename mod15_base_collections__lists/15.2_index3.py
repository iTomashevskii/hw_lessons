#Задача 3. Собачьи бега
#В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков за сезон.
# На огромном табло выводятся очки каждой собаки. Однако при выводе был обнаружен баг:
# собаки с наибольшим и наименьшим количеством очков поменялись местами! Нужно это исправить.
# Дан список очков из N собак. Напишите программу, которая меняет местами наибольший и наименьший элементы в списке.

scores = []
N = int(input('Кол-во чисел в списке: '))
for _ in range(N):
	num = int(input('Очередное число: '))
	scores.append(num)
maximum = scores[0]
minimum = scores[0]
icount = -1
for i in scores:
	icount += 1
	if maximum < i:
		maximum = i
		imax = icount
	if minimum > i:
		minimum = i
		imin = icount
scores[imax] = minimum
scores[imin] = maximum
print(scores)