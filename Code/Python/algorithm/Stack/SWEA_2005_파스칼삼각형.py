T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N+1)] for a in range(N)]  # 제일 왼쪽 열 0으로 padding

    # 첫 줄은 항상 1(가장 왼쪽 열은 padding)
    arr[0][1] = 1
    for i in range(1, N):
        for j in range(1, i+2):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]  # 왼쪽 위 + 오른쪽 위

    print('#{}'.format(test_case))
    for i in range(N):
        for j in range(N+1):
            if arr[i][j] != 0:
                print(arr[i][j], end=' ')
        print()