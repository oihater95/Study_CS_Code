T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int, input().split())  # N = 상자 수, Q = 수행 횟수
    box = [0 for i in range(N)]  # 초기 상태: 0

    for i in range(1, Q+1):  # 상자번호 1번부터 시작
        L, R = map(int, input().split())  # L: 시작 번호, R: 끝 번호

        for j in range(L-1, R):  # 인덱스는 0부터 시작
            box[j] = i

    print('#{} {}'.format(test_case, ' '.join(map(str, box))))
