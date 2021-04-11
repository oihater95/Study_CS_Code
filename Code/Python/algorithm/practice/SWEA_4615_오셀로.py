def switch(b):
    global row
    global col
    global color

    for j in range(N):
        for k in range(N):
            # 놓을 위치와 놓여있던 위치에 흰색만 놓여있을 경우 switch
            if b[j][k] == color:  # 현재 놓을 돌과 이전에 놓여있던 같은 색돌 비교하여 어느 위치에서 온 것인지 검색
                L = max(abs(row - j), abs(col - k))  # 현재 놓을 돌과 이전에 놓인 돌 사이 최대 몇칸인지
                if L < 2:
                    break
                if row == j or row == j + L or row == j - L or col == k or col == k + L or col == k - L:  # 가로 세로 대각선 위치인지
                    # 세로
                    if row > j:
                        # 하 세로
                        if col == k:
                            for m in range(1, L):
                                if b[j + m][k] == color or b[j + m][k] == 0:  # 사이에 같은색이나 비어있으면 break
                                    break
                            else:  # 사이에 있는 것이 모두 다른색 돌이면 현재 색으로 바꾸고 현재 놓을 위치에 추가
                                for n in range(1, L):
                                    b[j + n][k] = color

                        # 우하 대각선
                        elif col > k:
                            for m in range(1, L):
                                if b[j + m][k + m] == color or b[j + m][k + m] == 0:
                                    break
                            else:
                                for n in range(1, L):
                                    b[j + n][k + n] = color

                        # 좌하 대각선
                        elif col < k:
                            for m in range(1, L):
                                if b[j + m][k - m] == color or b[j + m][k - m] == 0:
                                    break
                            else:
                                for n in range(1, L):
                                    b[j + n][k - n] = color

                    elif row < j:  # 세로
                        # 상 세로
                        if col == k:
                            for m in range(1, L):
                                if b[j - m][k] == color or b[j - m][k] == 0:
                                    break
                            else:
                                for n in range(1, L):
                                    b[j - n][k] = color

                        # 좌상 대각선
                        elif col < k:
                            for m in range(1, L):
                                if b[j - m][k - m] == color or b[j - m][k - m] == 0:
                                    break
                            else:
                                for n in range(1, L):
                                    b[j - n][k - n] = color
                        # 우상 대각선
                        elif col > k:
                            for m in range(1, L):
                                if b[j - m][k + m] == color or b[j - m][k + m] == 0:
                                    break
                            else:
                                for n in range(1, L):
                                    b[j - n][k + n] = color

                    elif row == j:  # 가로
                        # 좌 가로
                        if col < k:
                            for m in range(1, L):
                                if b[j][k - m] == color or b[j][k - m] == 0:
                                    break
                            else:
                                for n in range(1, L):
                                    b[j][k - n] = color

                        # 우 가로
                        elif col > k:
                            for m in range(1, L):
                                if b[j][k + m] == color or b[j][k + m] == 0:
                                    break
                            else:
                                for n in range(1, L):
                                    b[j][k + n] = color
                else:
                    break

    b[row][col] = color
    return b


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())  # N = 보드의 크기, M = 플레이어가 돌을 놓는 횟수
    board = [[0 for _ in range(N)] for a in range(N)]
    board[N // 2 - 1][N // 2 - 1], board[N // 2][N // 2] = 2, 2  # 초기 백돌 위치, 백돌 = 2
    board[N // 2][N // 2 - 1], board[N // 2 - 1][N // 2] = 1, 1  # 초기 흑돌 위치, 흑돌 = 1
    cnt_w = 0  # 백돌 세기
    cnt_b = 0  # 흑돌 세기
    print()
    print(board)
    for i in range(M):
        col, row, color = map(int, input().split())
        col = col - 1  # 인덱스는 0부터 시작
        row = row - 1  # 인덱스는 0부터 시작
        print(i)
        board = switch(board)
        print(board)

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt_b += 1
            elif board[i][j] == 2:
                cnt_w += 1

    print('#{} {} {}'.format(test_case, cnt_b, cnt_w))