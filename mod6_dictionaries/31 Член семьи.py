# Дана структура, которая содержит описание одного из членов семьи (имя, фамилия, хобби, сколько лет и дети):
# Напишите программу, которая реализует такую структуру: имя, фамилия, хобби, кол-во лет и дети.
# Затем, с помощью метода get и установки значения по умолчанию, проверьте есть ли ребёнок с именем Bob.
# Затем в отдельную переменную получите фамилию этого ребёнка и выведите её на экран.
# Если у него нет фамилии, то получите значение ‘Nosurname’.

family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

childrens_dict = {}
for child in family_member["children"]:
    childrens_dict[child["name"]] = child["age"]

search_bob = childrens_dict.get("Bob", None)
if search_bob:
    print("Bob найден")
else:
    print("Bob-а нету!")

childrens_surname = family_member.get("surname", None)
if childrens_surname:
    print(childrens_surname)
else:
    print("Nosurname")

# ----------------мое----------------------------------------
# if 'Bob' in family_member.get('children', {})[1].get('name'):
#     print('yo')
# for child in family_member.get('children', {})[1]:
#     if child == 'Bob':
#         child_surname = child.get('surname', 'Nosurname') --- не работает((
# print(child_surname)
