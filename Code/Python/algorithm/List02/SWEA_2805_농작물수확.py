T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 농장 크기 N X N
    arr = []
    result = 0

    for i in range(N):
        arr.append(list(map(int, input())))

    for i in range(N//2 + 1):
        for j in range(N//2-i, N//2+i+1):
            if i == N//2:
                result += arr[i][j]
            else:
                result += arr[i][j] + arr[N-i-1][j]

    print('#{} {}'.format(test_case, result))