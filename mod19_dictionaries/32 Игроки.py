# Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет,
# а также его текущий статус, в котором указано, отдыхает он, тренируется или путешествует:
players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}
# Напишите программу, которая выводит на экран вот такие данные в разных строчках:
#
# 1 - Все члены команды из команды А, которые отдыхают.
# 2 - Все члены команды из группы B, которые тренируются.
# 3 - Все члены команды из команды C, которые путешествуют.

#---------------------------решение sb --------------------------
# Чтобы не прописывать решение "в лоб", вручную подставляя статус и команду - попробуем сформировать дополнительные словарь и список,
# чтобы автоматизировать этот процесс:
help_dict = {"Rest": "отдыхают",
             "Training": "тренируются",
             "Travel": "путешествуют"}

team_order = ["A", "B", "C"]

# Запустим цикл по словарю состояний и одновременно будем вести счёт состояний, чтобы на каждой итерации выбирать одну из команд:
for index, state in enumerate(help_dict):
    print(f"Все члены команды из команды {team_order[index]}, которые {help_dict[state]}:")
    for _, player in players_dict.items():
        if player["status"] == state and player["team"] == team_order[index]:
            print(player["name"])

# --------------------------мое решение---------------------------
# a_rest_players = [
# 	player['name']
# 	for player in players_dict.values()
# 	if player['team'] == 'A' and player['status'] == 'Rest'
# ]
# print(f'{a_rest_players}')
#
# b_train_players = [
# 	player['name']
# 	for player in players_dict.values()
# 	if player['team'] == 'B' and player['status'] == 'Training'
# ]
# print(f'{b_train_players}')
#
# c_travel_players = [
# 	player['name']
# 	for player in players_dict.values()
# 	if player['team'] == 'C' and player['status'] == 'Travel'
# ]
# print(f'{c_travel_players}')
# --------------------------решение---------------------------