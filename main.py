import random

#수도 맞히기 게임 함수
def capital_game():
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
        '사우디아라비아': '리야드',
        '남아프리카공화국': '프리토리아',
        '이집트': '카이로',
        '터키': '앙카라',
        '이란': '테헤란',
        '태국': '방콕',
        '스페인': '마드리드',
        '네덜란드': '암스테르담',
        '스위스': '베른',
        '그리스': '아테네',
        '벨기에': '브뤼셀',
        '오스트리아': '비엔나',
        '노르웨이': '오슬로',
        '스웨덴': '스톡홀름',
        '덴마크': '코펜하겐',
        '핀란드': '헬싱키',
        '포르투갈': '리스본',
        '폴란드': '바르샤바',
        '체코': '프라하',
        '헝가리': '부다페스트',
        '아일랜드': '더블린',
        '우크라이나': '키예프',
        '루마니아': '부쿠레슈티',
        '뉴질랜드': '웰링턴',
        '말레이시아': '쿠알라룸푸르',
        '필리핀': '마닐라',
        '싱가포르': '싱가포르',
        '인도네시아': '자카르타',
        '베트남': '하노이',
        '칠레': '산티아고',
        '콜롬비아': '보고타',
        '베네수엘라': '카라카스',
        '페루': '리마'
    }
    countries = list(countries_capitals.keys())

    players = ['민주', '주형', '하영', '용화', '영헌']
    current_player = 0

    while True:
        country = random.choice(countries)
        capital = countries_capitals[country]
        answer = input("{}님, {}의 수도는 어디일까요? ".format(players[current_player], country))
        if answer == capital:
            print("어케알았노!")
            current_player = (current_player + 1) % len(players)
        else:
            print("땡. 한 잔 마시세요~ {}의 수도는 {}이거든~".format(country, capital))
            break


gamestate = False
drinklimit = 0

#게임 시작시 필요한 정보 받는 함수
def gamestart():
    global gamestate, drinklimit, username
    start = input("게임을 진행할까요? (y/n) : ")
    if (start == 'y'):
        gamestate = True
    else:
        gamestate = False
        return
    username = input('오늘 거하게 취해볼 당신의 이름은? : ')
    while True:    
        try:
            drinklimit = input("""~~~~~~~~~~~~~~~~~~~~~~🍺 소주 기준 당신의 주량은? 🍺~~~~~~~~~~~~~~~~~~~~~~
                        🍺 1. 소주 반병(2잔)
                        🍺 2. 소주 반병에서 한병(4잔)
                        🍺 3. 소주 한병에서 한병 반(6잔)
                        🍺 4. 소주 한병 반에서 두병(8잔)
                        🍺 5. 소주 두병 이상(10잔)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                        
당신의 치사량(주량)은 얼마만큼인가요?(1~5을 선택해주세요) : """)
            drinklimit = int(drinklimit)*2
            if not (0<drinklimit<12):
                print('보기에서 선택해주세요!')
            else:
                break
        except ValueError:
            print('숫자를 입력해주세요!')

gamestart()

#플레이어 정보 받는 부분
playerlist = ['은서', '하연', '연서', '예진', '헌도']
playernum = 0
players = []
def playerselect(username, drinklimit):
    try:
        global playernum, playerlist, players
        playernum = input('함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : ')
        
        #친구 초대수만큼 반복
        for _ in range(int(playernum)):
            #npc 정보 추가
            random_player = random.choice(playerlist)
            random_drink_limit = random.choice([2, 4, 6, 8, 10])
            players.append({'name': random_player, 'drink_limit': random_drink_limit})
            print(f"오늘 함께 취할 친구는 {random_player}입니다! (치사량 :{random_drink_limit})")
        #유저정보 마지막에 추가
        players.append({'name': username, 'drink_limit': drinklimit})

    except ValueError:
        print('숫자를 입력해주세요!')
    #유저의 마신 잔 수, 남은 치사량 출력
    print("~"*74)
    for player in players:
        print("{0}는 지금까지 {1}🍺! 치사량까지 {2}".format(player['name'], "0", player['drink_limit']))

playerselect(username, drinklimit)

print("~"*74)

print("""~~~~~~~~~~~~~~~~~~~~~~🍺 오늘의 ALCOHOL GAME 🍺~~~~~~~~~~~~~~~~~~~~~~
                        🍺 1. 수도 맞히기 게임
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

game_type = input("{0}이(가) 좋아하는 랜덤 게임~ 무슨 게임~ 게임 start~ 게임 start~: ".format(username))

print("{}님이 게임을 선택하셨습니다!".format(username))


if game_type == '1' :
    capital_game()

# print(players)

#게임이 끝날때까지 도는 loop
#while gamestate==True:
    
    

