#Аркадий как-то раз написал программу для вывода таблицы степеней для определённых чисел.
# Недавно он узнал про такую штуку, как списки, и решил программу немного переписать, а заодно усовершенствовать её.
# По его задумке, вначале есть всего три числа: 3, 7 и 5, а затем с помощью бесконечного цикла программа
# запрашивает новое число, закидывает его в конец текущего списка чисел и выводит вторую, третью и четвёртую
# степень каждого числа текущего списка.

numbers = [3,7,5]
while True:
  number = int(input('Новое число: '))
  numbers.append(number)
  print('Текущий список чисел:', numbers)
  for _ in numbers:
    print(_ ** 2, _ ** 3, _ ** 4)
  print()