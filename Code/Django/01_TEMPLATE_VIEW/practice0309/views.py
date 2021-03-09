from django.shortcuts import render
from django.shortcuts import HttpResponse
import random
import requests  # 클라이언트

# Variable Route
def var_route(request, value):  # urls.py에서 받은 <string> 받아줘야함
    return HttpResponse(value)


def lotto(request, value):
    # 현실 당첨 번호, value = 회차
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=' + value
    res = requests.get(url)
    data_dict = res.json()
    win_nums = []
    people = []
    wins = [0] * 6  # 등수

    # 당첨 번호
    for i in range(1, 7):
        num = 'drwtNo'
        num += str(i)
        win_nums.append(data_dict[num])
    # 보너스 번호
    bonus_num = data_dict['bnusNo']

    # 1000명이 로또 뽑음
    for i in range(1000):
        a = random.sample(range(1, 46), 6)
        people.append(a)

    # 등수
    for i in range(1000):
        cnt = 0
        for j in range(6):
            if win_nums[j] in people[i]:
                cnt += 1
        
        if cnt == 6:  # 1등
            wins[0] += 1
        elif cnt == 5:
            if bonus_num in people:
                wins[1] += 1  # 2등
            else:
                wins[2] += 1  # 3등
        elif cnt == 4:
            wins[3] += 1  # 4등
        elif cnt == 3:
            wins[4] += 1  # 5등
        else:
            wins[5] += 1  # 꽝

    context = {
        'win_nums': win_nums,
        'bonus_num': bonus_num,
        'wins': wins[:5],  # 1 ~ 5등
        'fail': wins[5],  # 꽝
        'value': value
    }

    return render(request, 'practice0309/lotto.html', context)

    
def lotto_sol(request):
    # 현실 당첨 번호
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'
    res = requests.get(url)
    data_dict = res.json()
    win_nums = []
 
    # 당첨 번호
    for i in range(1, 7):
        num = 'drwtNo'
        num += str(i)
        win_nums.append(data_dict[num])
    # 보너스 번호
    bonus_num = data_dict['bnusNo']

    result = {f'{i}등': 0 for i in range(1, 6)}
    result['꽝'] = 0

    for _ in range(1000):
        my_numbers = random.sample(range(1, 46), 6)
        cnt = len(set(win_nums) & set(my_numbers))

        if cnt == 6:  # 1등
            result['1등'] += 1

        elif cnt == 5:
            if bonus_num in my_numbers:
                result['2등'] += 1  # 2등
            else:
                result['3등'] += 1  # 3등

        elif cnt == 4:
            result['4등'] += 1  # 4등

        elif cnt == 3:
            result['5등'] += 1  # 5등

        else:
            result['꽝'] += 1  # 꽝

    context = {
        'win_nums': win_nums,
        'bonus_num': bonus_num,
        'result': result,  
        
    }

    return render(request, 'practice0309/lotto_sol.html', context)


# 사용자 입력할 form & input용 HTML 제공 (URL에 데이터를 담음)
def ping(request):
    return render(request, 'practice0309/ping.html')


def pong(request):
    # 안 씀 X, 
    # input에 name없는 경우: value는 넘어왔지만 key가 없음 => 아무것도 넘어오지 않는다
    # input에 name붙여줘야 key: value 값으로 넘어옴 => request에 담겨 있음
    qd = request.GET  # <QueryDict: {'kr-name': ['문성호'], 'en-name':['Moon']}
    kr_name = request.GET['kr-name']  # []을 쓰면 없는 경우 에러, <input name = 'kr-name'>
    en_name = request.GET.get('en-name')  # .get()을 쓰면 없는 경우 none
    fullname = kr_name + en_name
    context = {
        'fullname': fullname,
    }
    return render(request, 'practice0309/pong.html', context)