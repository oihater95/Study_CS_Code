def bfs(r, c, cnt):
    que.append((r, c, cnt))
    while que:  # 큐가 비어있지 않다면
        size = len(que)  # 큐의 크기만큼 반복 (같은 거리 그룹화)
        for s in range(size):
            temp = que.pop(0)
            r, c = temp[0], temp[1]

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                maze[r][c] = 1  # 방문체크
                if 0 <= nr < N and 0 <= nc < N:  # 미로 범위 안을 벗어나지 않는다.
                    if maze[nr][nc] == 3:  # 도착점
                        return cnt

                    elif maze[nr][nc] == 0:  # 통로
                        que.append((nr, nc, cnt))
        cnt += 1

    return 0

for tc in range(1, int(input())+1):
    N = int(input())  # 미로의 크기
    maze = []  # 미로 행렬
    que = []
    count = 0  # 거리

    for i in range(N):
        maze.append(list(map(int, input())))

    for i in range(N):
        for j in range(N):
            # 시작점
            if maze[i][j] == 2:
                row = i
                col = j
    # 상우하좌 시계방향
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    print('#{} {}'.format(tc, bfs(row, col, count)))