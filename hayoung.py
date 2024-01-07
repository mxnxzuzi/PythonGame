import random

def get_random_vs_pair():
    with open('vs.txt', 'r', encoding='utf-8') as file: 
        lines = file.readlines()
        return random.choice(lines).strip()

def play_egudongseong_game(player_name, friends):
    vs_pair = get_random_vs_pair()
    choices = vs_pair.split(' vs ')
    print(f"{vs_pair} - 선택하세요!")

    player_choices = {}
    total_players = [player_name] + friends

    if len(total_players) == 4:  # 플레이어가 4명인 경우
        teams = [total_players[:2], total_players[2:]]
        print(f"{teams[0][0]}과 {teams[0][1]}이 1팀이고, {teams[1][0]}과 {teams[1][1]}은 2팀입니다.")
        results = []

        for team in teams:
            team_choice = set()
            for member in team:
                if member == player_name:
                    while True:
                        choice = input(f"{player_name}의 선택: ")
                        if choice in choices:
                            break
                        else:
                            print("잘못된 값입니다. 다시 입력하세요.")
                else:
                    choice = random.choice(choices)
                team_choice.add(choice)
                results.append({'name': member, 'choice': choice, 'lost': False})
            
            team_win = len(team_choice) == 1
            for result in results:
                if result['name'] in team:
                    result['lost'] = not team_win

        return results
    else:  # 그 외의 경우
        player_choices[player_name] = input(f"{player_name}의 선택: ")
        for friend in friends:
            player_choices[friend] = random.choice(choices)
        all_same = len(set(player_choices.values())) == 1
        return [{'name': name, 'choice': choice, 'lost': not all_same} for name, choice in player_choices.items()]
