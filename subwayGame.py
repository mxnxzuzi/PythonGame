import json
import random

def start_game(line_num_dict):
    print("🚇 지하철~지하철~지하철~지하철 🚇 🤔 몇호선~몇호선~몇호선~몇호선~ 🤔")
    random_line_num = random.choice(list(line_num_dict.keys()))
    print(f"[{random_line_num}]")

    used_stations = set()

    players = initialize_players()

    while True:
        for player in players:

            selected_station = input(f"{player['name']}, 어떤 역을 선택하시겠습니까?🤔 ")

            if selected_station in used_stations:
                print("어❓❓ 🤣바보샷ㅋ🍻 🤣바보샷ㅋ🍻")
                exit()

            if selected_station not in line_num_dict[random_line_num]:
                print(f"🤪 아 누가 술을 마셔 🤪 {player['name']}가 술을마셔~ 🍻 원~ 샷~ ☠️")
                exit()

            used_stations.add(selected_station)
            player['current_station'] = selected_station
            
            if not used_stations:
                print("모든 역을 다 선택하셨습니다. 게임 종료!")
                exit()

def initialize_players():
    player_names = ["짱구", "유리", "훈이", "철수", "맹구"]
    players = []

    for i in range(1, 6):
        player_name = random.choice(player_names)

        player = {
            "id": i,
            "name": player_name,
            "current_station": None  
        }
        players.append(player)

    return players

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

start_game(line_num_dict)
