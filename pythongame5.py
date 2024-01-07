#!pip install BeautifulSoup4
#!pipinstall requests
#슈퍼개미게임 : 임의의 주식이 오늘 올랐는지, 떨어졌는지 선택하면 되는 간단한 게임입니다! 틀리면 마셔~! 
import random
import requests
from bs4 import BeautifulSoup as bs

url="https://finance.naver.com/"

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"} #네이버 페이지 입장용 헤더
response=requests.get(url, headers=header)

soup = bs(response.text, 'html.parser')

top_items_tbody = soup.find('tbody', {'id': '_topItems1'}) #주식 거래 top 

item_names = [a.text for a in top_items_tbody.find_all('a')] #주식 이름
item_change = [span.text for span in top_items_tbody.find_all('span')] #주식 상승, 하락
item_change_value = [tr.find_all('td')[2].text for tr in top_items_tbody.find_all('tr')] # 주식 상승 하락 값

player = 3
playerlist = ['은서', '하연', '연서', '예진', '헌도']
username = '연서'

number_range = range(0, len(item_names)-1)
num_of_random_numbers = player+1
random_numbers = random.sample(number_range, num_of_random_numbers)

def antgame(player):
    print('개미는~뚠뚠!🐜 오늘도~뚠뚠!🐜 열심히~주식~하네~🐜 오늘의 주식이 상승했는지 하강했는지 맞춰보세요!')
    for i in range(player+1):
        print(playerlist[i],'님 차례입니다')
        print(item_names[random_numbers[i]],'는 오늘 상승했을까요? 하락했을까요?')
        if(playerlist[i]==username):
            answer=input('1.상승 2.하락 :')
        else:
            answer=random.choice(['1', '2'])
        if((answer=='1' and item_change[random_numbers[i]]=='상승') or (answer=='2' and item_change[random_numbers[i]]=='하락')):
            print("정답입니다! 촉이 좋은 개미시군요!!😎")
        else:
            print("당신은 주식하면 큰일나겠네요!😮")
            #player[i].주량 -

antgame(player)
