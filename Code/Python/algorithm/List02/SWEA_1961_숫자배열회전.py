T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # N x N 행렬
    arr = [list(map(int, input().split())) for _ in range(N)]
    rotate_90, rotate_180, rotate_270 = [[0 for i in range(N)] for j in range(N)], \
                                        [[0 for i in range(N)] for j in range(N)], [[0 for i in range(N)] for j in range(N)]

    for i in range(N):  # 회전 행렬
        for j in range(N):
            rotate_90[i][j] = arr[N-1-j][i]  # 90도 회전
            rotate_180[i][j] = arr[N-1-i][N-1-j]  # 180도 회전
            rotate_270[i][j] = arr[j][N-1-i]  # 270도 회전

    print('#{}'.format(test_case))

    for i in range(N):
        print(''.join(map(str, rotate_90[i])),
                      ''.join(map(str, rotate_180[i])), ''.join(map(str, rotate_270[i])))

