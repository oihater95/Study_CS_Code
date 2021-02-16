T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input(). split())
    arr = []
    max_result = 0

    for i in range(N):
        arr.append(list(map(int, input().split())))  # 파리 좌표

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            result = 0
            for k in range(M):
                for l in range(M):
                    result += arr[i+k][j+l]  # 파리채 구역 당 얼마나 잡았는지
            if max_result < result:  # 최대 잡은 수
                max_result = result

    print('#{} {}'.format(test_case, max_result))