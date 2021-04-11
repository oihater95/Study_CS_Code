def check():
    ans = 'Possible'

    for i in range(last+1):
        if i != 0 and i % M == 0:  # M초 마다 붕어빵 생성 0초부터 시작
            for j in range(K):  # K개의 붕어빵
                snack.append(1)

        while i in reserve:
            if snack:  # 남는 붕어빵 존재
                snack.pop()
                reserve.remove(i)
            else:
                ans = 'Impossible'
                return ans
    return ans

T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())  # N: 손님 수 M: 붕어빵 만드는데 걸리는 시간 K: 붕어빵 수
    reserve = list(map(int, input().split()))  # 예약손님이 오는 시간
    reserve = sorted(reserve)  # 시간 순서대로 정렬
    last = max(reserve)  # 가장 마지막 손님
    snack = []  # 남은 붕어빵 stack

    print('#{} {}'.format(test_case, check()))

###############################################################
T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # 사람 수, 붕어빵 시간, 붕어빵 개수
    reserved = list(map(int, input().split()))
    reserved.sort()  # 순서대로 정렬

    bread = 0
    for r in range(len(reserved)):
        if (reserved[r] // M) * K < r + 1:
            print('#{} Impossible'.format(tc))
            break
    else:
        print('#{} Possible'.format(tc))