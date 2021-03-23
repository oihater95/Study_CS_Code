def BFS(r, c):
    que.append((r, c))
    while que:
        temp = que.pop(0)
        row, col = temp[0], temp[1]  # 현재 행, 열
        arr[row][col] = 1  # 방문체크

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < N and 0 <= nc < N:  # 미로 영역 안
                if arr[nr][nc] == 3:  # 도착점 도달
                    return 1
                elif arr[nr][nc] == 0:  # 통로일 경우 해당 지점을 시작점으로 거리 1이고 벽 아닌 지점들 큐에 추가
                    que.append((nr, nc))

    return 0  # 도착점 도달 못함

for tc in range(1, 11):
    t = int(input())
    N = 100
    arr = []
    que = []
    # 상우하좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for i in range(N):
        arr.append(list(map(int, input())))

    for i in range(N):
        for j in range(N):
            # 시작점
            if arr[i][j] == 2:
                ans = BFS(i, j)

    print('#{} {}'.format(tc, ans))
