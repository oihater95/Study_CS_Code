T = int(input())

for test_case in range(1, T+1):
    day = int(input())
    buy = list(map(int, input().split()))
    max_idx = 0  # 최대값 인덱스
    max_cost = buy[max_idx]  # 최대값
    idx = 0  # 구간 인덱스
    income = 0
    # 최대값 전까지는 사고 최대값일 때 팔기, 이후 구간에서의 최대값전까지 사고 최대값일 때 팔기 반복
    while idx < day:

        # 구간 최대값 찾기
        max_idx = idx
        max_cost = buy[max_idx]

        # 구간 최대값(이전 구간 + 1 ~ 최대값)
        for i in range(idx, day):
            if buy[i] >= max_cost:  # 현재 인덱스의 값이 최대값보다 클 때
                max_cost = buy[i]
                max_idx = i

        # 구간 수익 계산
        for i in range(idx, max_idx):
            income += max_cost - buy[i]

        if max_idx == idx:  # 최대값이 구간 시작값이면 다음 인덱스로
            idx += 1
        else:
            idx = max_idx  # 구간 인덱스 갱신

    print('#{} {}'.format(test_case, income))

#####################################################################################
# 뒤에서부터 세기
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    costs = list(map(int, input().split()))
    answer = 0
    my_max = costs[N - 1]
    for i in range(N - 2, -1, -1):
        if my_max > costs[i]:
            answer += my_max - costs[i]
        elif my_max < costs[i]:
            my_max = costs[i]

    print('#{} {}'.format(tc, answer))