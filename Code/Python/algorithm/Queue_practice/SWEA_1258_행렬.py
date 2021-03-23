def rowcolsize(r, c):

    idx = 0
    row = 0
    while 0 <= r+idx < N and arr[r + idx][c] != 0:  # 행 크기
        row += 1
        idx += 1

    idx = 0
    col = 0
    while 0 <= c + idx < N and arr[r][c + idx] != 0:  # 열 크기
        col += 1
        idx += 1

    for i in range(row):
        for j in range(col):
            arr[r+i][c+j] = 0  # 방문체크

    arr_size.append((row*col, row, col))  # 곱 크기, 행 크기, 열 크기


for tc in range(1, int(input())+1):
    N = int(input())  # 전체 크기
    arr = []  # 입력배열
    arr_size = []  # 행렬 크기 모아둔 리스트

    for i in range(N):
        arr.append(list(map(int, input().split())))

    # 시작점
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                rowcolsize(i, j)

    # sorted (x[0]을 기준으로 먼저 정렬 후 x[1] 기준으로 정렬)
    ans = sorted(arr_size, key=lambda x: (x[0], x[1]))

    print('#{} {}'.format(tc, len(ans)), end=' ')
    for i in range(len(ans)):
        print('{} {}'.format(ans[i][1], ans[i][2]), end= ' ')
    print()