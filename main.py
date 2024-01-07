import random

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

playerselect(username, drinklimit)
print(players)

#게임이 끝날때까지 도는 loop
#while gamestate==True:
    
    


