def switch(b):
    # 8방향
    for i in range(8):
        cnt = 0  # 같은 색 돌까지 몇 칸
        nr = row
        nc = col

        # 숫자있는 경우, 보드 내부
        while nr + dr[i] >= 0 and nr + dr[i] < N and nc + dc[i] >= 0 and nc + dc[i] < N and b[nr+dr[i]][nc+dc[i]]:
            # 같은 색의 돌을 만나면 중간에 다른색의 돌을 바꿈
            if abs(b[nr+dr[i]][nc+dc[i]] - b[row][col]) == 0:
                for j in range(1, cnt+1):
                    nr = row
                    nc = col
                    b[nr + dr[i]*j][nc + dc[i]*j] = color
                break
            # 다른 색 돌 만남
            elif b[nr+dr[i]][nc+dc[i]] != 0 and abs(b[nr+dr[i]][nc+dc[i]] - b[row][col]) == 1:
                cnt += 1  # 같은 색 돌까지 +1
                nr += dr[i]
                nc += dc[i]

    return b


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())  # N = 보드의 크기, M = 플레이어가 돌을 놓는 횟수
    board = [[0 for _ in range(N)] for a in range(N)]
    board[N // 2 - 1][N // 2 - 1], board[N // 2][N // 2] = 2, 2  # 초기 백돌 위치, 백돌 = 2
    board[N // 2][N // 2 - 1], board[N // 2 - 1][N // 2] = 1, 1  # 초기 흑돌 위치, 흑돌 = 1
    cnt_w = 0  # 백돌 세기
    cnt_b = 0  # 흑돌 세기
    # 8방향 우 부터 시계방향
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    for i in range(M):
        col, row, color = map(int, input().split())
        col = col - 1  # 인덱스는 0부터 시작
        row = row - 1  # 인덱스는 0부터 시작
        board[row][col] = color  # 이번 회차에 놓은 돌
        board = switch(board)

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt_b += 1
            elif board[i][j] == 2:
                cnt_w += 1

    print('#{} {} {}'.format(test_case, cnt_b, cnt_w))