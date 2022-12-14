# Мы работаем в одной небольшой торговой компании, где все данные о продажах фруктов за год сохранены в словаре
# в виде пар «название фрукта — доход»:
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
# В компании наступил небольшой кризис, и нам поручено провести небольшой анализ дохода.
# Напишите программу, которая находит общий доход, затем выводит фрукт с минимальным доходом и удаляет его из словаря.
# Выведите итоговый словарь на экран.
# Результат работы программы:
# Общий доход за год составил 35419.34 рублей
# Самый маленький доход у grapefruit. Он составляет 300.4 рублей
# Итоговый словарь: {'apple': 5600.2, 'orange': 3500.45, 'banana': 5000.0, 'bergamot': 3700.56, 'durian': 5987.23,
#                    'peach': 10000.5, 'pear': 1020.0, 'persimmon': 310.0}

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
# --------------------------------------------------------------------------------------------------------
# топовое решение
def get_value(x):
    return x[1]


result_sum = sum(incomes.values())
min_name, min_value = min(incomes.items(), key=get_value)
# При помощи функции и параметра key мы говорим пайтону как именно надо сравнивать между собой элементы
# Т.к. элементы записаны в таком виде - ('apple': 5600.20), а сравнивать мы хотим по значениям - то нам проосто надо брать для сравнения
# элементы под индексом 1 (если бы сравнивали по ключам, то индекс надо было бы заменить на 0)
print(result_sum, min_name, min_value)
# --------------------------------------------------------------------------------------------------------
# как надо было:

# result_sum = 0
# min_value = None
# min_name = ""
# for name, value in incomes.items():  # items() позволяет сразу обратиться и к ключам, и к значениям словаря
#     result_sum += value
#     if min_value is None or min_value > value:
#         min_value = value
#         min_name = name
#
# incomes.pop(min_name)
#
# print(f"Общий доход за год составил {result_sum} рублей")
# print(f"Самый маленький доход у {min_name}. Он составляет {min_value} рублей")
# print("Итоговый словарь:", incomes)
# --------------------------------------------------------------------------------------------------------
# мое - хрень, выше из решения

# total_income = 0
# for income in incomes.values():
#     total_income += income
# for key in incomes.keys():
#     if incomes[key] == min(incomes.values()):
#         outsider = key
#
# print(f'Общий доход за год составил {total_income} рублей\n'
#       f'Самый маленький доход у {outsider}. Он составляет {min(incomes.values())} рублей')
# incomes.pop(outsider)
# print('Итоговый словарь: ')
# for good in incomes:
#     print(f'{good}: {incomes[good]}')