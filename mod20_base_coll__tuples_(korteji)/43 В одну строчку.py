# Нашему другу дали задачу: «Есть словарь, в котором ключи — это числа от 0 до 4,
# а значения ключей — числа 0, 100, 144, 20 и 19 соответственно. Нужно написать программу, которая выводит список тех значений,
# у которых ключ делится на 2. Причём программа должна быть в одну строчку.»
# Программа у друга работает, но её не приняли, так как в ней не используется правило «не повторяйся» — это когда части кода не повторяются.
# Помогите другу исправить решение задачи так, чтобы код в строчке не повторялся.
# Решение друга:
# print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19} if i_key % 2 == 0])
print([i_value for i_key, i_value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])