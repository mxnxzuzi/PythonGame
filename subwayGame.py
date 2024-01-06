import json
import random

with open('sub.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

line_num_dict = {}

for entry in data:
    line_num = entry.get("line_num", "")
    station_nm = entry.get("station_nm", "")

    if line_num in line_num_dict:
        line_num_dict[line_num].append(station_nm)
    else:
        line_num_dict[line_num] = [station_nm]

for line_num, station_nms in line_num_dict.items():
    print(f"Line {line_num}:")
    for station_nm in station_nms:
        print(f" - {station_nm}")
    print()

player_names = ["짱구", "유리", "훈이", "철수", "맹구"]

players = []

for i in range(1, 6):

    player_name = random.choice(player_names)

    player = {
        "id": i,
        "name": player_name,
    }
    players.append(player)

