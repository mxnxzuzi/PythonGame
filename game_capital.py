import random

#수도 맞히기 게임 함수
def capital_game(player_name, friends):
    countries_capitals = {
        '대한민국': '서울',
        '미국': '워싱턴 D.C.',
        '일본': '도쿄',
        '중국': '베이징',
        '영국': '런던',
        '프랑스': '파리',
        '독일': '베를린',
        '이탈리아': '로마',
        '캐나다': '오타와',
        '호주': '캔버라',
        '러시아': '모스크바',
        '인도': '뉴델리',
        '브라질': '브라질리아',
        '아르헨티나': '부에노스아이레스',
        '멕시코': '멕시코시티',      
        '이집트': '카이로',
        '태국': '방콕',
        '스페인': '마드리드',
        '그리스': '아테네',
        '스웨덴': '스톡홀롬',
        '덴마크': '코펜하겐',
        '핀란드': '헬싱키',
        '포르투갈': '리스본',
        '필리핀': '마닐라',
    }
    countries = list(countries_capitals.keys())
    token = 0
    current_player = 0

    while True:
        for player in friends:
            country = random.choice(countries)
            capital = countries_capitals[country]

            if player['name'] != player_name:
                if random.random() < 0.2:
                    answer = "뭐였지..?"
                else:
                    answer = capital
                print("{}님, {}의 수도는 어디일까요? {}".format(player['name'], country, answer))
            else:
                answer = input("{}님, {}의 수도는 어디일까요? ".format(player['name'], country))

            if answer == capital:
                print("어케알았노!")
                current_player = (current_player + 1) % len(friends)
            else:
                print("땡. 한 잔 마시세요~ {}의 수도는 {}거든~".format(country, capital))
                token = 1
                break
        if token == 1:
            return [player['name']]
