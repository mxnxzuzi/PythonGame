import random
import hayoung
#***********여기에 각자 게임 모듈 임포트*********
#***********여기에 각자 게임 모듈 임포트*********
#***********여기에 각자 게임 모듈 임포트*********
#***********여기에 각자 게임 모듈 임포트*********

gamestate = False
drinklimit = 0

def gamestart():
    global gamestate, drinklimit, username
    print(print("""
          --------------------------------------------------
          --------------------------------------------------

          TEAM 1 MINI GAME !

          --------------------------------------------------
          --------------------------------------------------

          """))
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
            drinklimit = int(drinklimit) * 2
            if not (0 < drinklimit <= 10):
                print('보기에서 선택해주세요!')
            else:
                break
        except ValueError:
            print('숫자를 입력해주세요!')

gamestart()

playerlist = ['은서', '하연', '연서', '예진', '헌도']
playernum = 0
players = []
def playerselect(username, drinklimit):
    try:
        global playernum, playerlist, players
        playernum = input('함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : ')
        
        for _ in range(int(playernum)):
           
            random_player = random.choice(playerlist)
            random_drink_limit = random.choice([2, 4, 6, 8, 10])
            players.append({'name': random_player, 'drink_limit': random_drink_limit})
            print(f"오늘 함께 취할 친구는 {random_player}입니다! (치사량 :{random_drink_limit})")
        
        players.append({'name': username, 'drink_limit': drinklimit})

    except ValueError:
        print('숫자를 입력해주세요!')
    
    for player in players:
        player['current_drinks'] = 0

playerselect(username, drinklimit)

def select_game():
    while True:
        print("""
          --------------------------------------------------
                       🍺오늘의 Alcohol GAME🍺
          --------------------------------------------------

                        1. 이구동성 게임
                        2.
                        3.
                        4.
                        5. 
    
          --------------------------------------------------
          --------------------------------------------------

          """)
        game_choice = input("실행하고 싶은 게임 번호를 선택해주세요 : ")
        if game_choice == "1":
            return hayoung.play_egudongseong_game(username, [player['name'] for player in players if player['name'] != username])
        
        #elif*************여기에 각자 게임추가하기*************
        #elif*************여기에 각자 게임추가하기*************
        #elif*************여기에 각자 게임추가하기*************
        #elif*************여기에 각자 게임추가하기*************

        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

def select_game_auto():
    game_choice = str(random.randint(1, 5)) 
    print("""
          --------------------------------------------------
                       🍺오늘의 Alcohol GAME🍺
          --------------------------------------------------

                        1. 이구동성 게임
                        2.
                        3.
                        4.
                        5. 
    
          --------------------------------------------------
          --------------------------------------------------

          """)
    user_input = input("술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 'exit'를, 계속하고 싶으면 아무 키나 입력해주세요: ")
    if user_input.lower() == 'exit':
        print("게임을 종료합니다.")
        global gamestate
        gamestate = False
        return None
    else:
        print(f"다음 게임은 {game_choice}번 게임입니다.")
        if game_choice == "1":
            return hayoung.play_egudongseong_game(username, [player['name'] for player in players if player['name'] != username])
        
        #elif*************여기에 각자 게임추가하기*************
        #elif*************여기에 각자 게임추가하기*************
        #elif*************여기에 각자 게임추가하기*************
        #elif*************여기에 각자 게임추가하기*************

    print("""
          --------------------------------------------------
          --------------------------------------------------

          NEW GAME START !

          --------------------------------------------------
          --------------------------------------------------

          """)
def check_game_end():
    for player in players:
        if player['drink_limit'] <= player['current_drinks']:
            return True
    return False
        

while gamestate:
    game_results = select_game()  
    if game_results:  
        for result in game_results:
            print(f"{result['name']}의 선택: {result['choice']}")
            if result['lost']:
                print(f"{result['name']}은 술을 마셔 원샷!")
                for player in players:
                    if player['name'] == result['name']:
                        player['current_drinks'] += 1

       
        for player in players:
            print("""
                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                  """
                  )
            print(f"{player['name']}은(는), 지금까지 {player['current_drinks']}🍺, 치사량까지 {player['drink_limit'] - player['current_drinks']}")

        
        if check_game_end():
            print("""
          --------------------------------------------------
          --------------------------------------------------

          GAME OVER !

          --------------------------------------------------
          --------------------------------------------------

          """)
            break

        
        game_results = select_game_auto()
        if not game_results:
            print("""
          --------------------------------------------------
          --------------------------------------------------

          GAME OVER !

          --------------------------------------------------
          --------------------------------------------------

          """)
            break



    
    

