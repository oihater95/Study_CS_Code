T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 농장 크기 N X N
    arr = []
    result = 0

    for i in range(N):  # 농장
        arr.append(list(map(int, input())))

    for i in range(N//2 + 1):  # 수확범위 마름모 설정 (1, N), (2, N-1), (3, N-2) ... 짝 설정
        for j in range(N//2-i, N//2+i+1):
            if i == N//2:  # 중간행은 짝이 없음
                result += arr[i][j]
            else:  # 1행 + N행, 2행 + N-1행, ...
                result += arr[i][j] + arr[N-i-1][j]

    print('#{} {}'.format(test_case, result))