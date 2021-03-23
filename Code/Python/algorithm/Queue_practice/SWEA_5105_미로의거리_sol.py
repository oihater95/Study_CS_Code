def bfs(r, c):
    # 선형큐
    Q = [0] * 1000000
    front = -1
    rear = 0
    Q[rear] = (r, c)
    dist = [[-1]*(N) for _ in range(N)]
    dist[r][c] = 0

    # 선형큐 공백검사
    while front != rear:
        front += 1
        curr_r, curr_c = Q[front]
        if maze[curr_r][curr_c] == '3':
            return dist[curr_r][curr_c] - 1
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            # padding안함 범위검사 해야함
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue

            #벽이 아니면서 거리를 갱신하지 않았다면 좌표넣고 갱신
            if maze[nr][nc] != '1' and dist[nr][nc] == -1:
                dist[nr][nc] = dist[curr_r][curr_c] + 1
                rear += 1
                Q[rear] = (nr, nc)
    return 0


# 시작 정점
def search():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j




for tc in range(1, int(input())+1):
    N = int(input())  # 미로의 크기
    maze = []  # 미로 행렬

    for i in range(N):
        maze.append(list(map(int, input())))

    # 상우하좌 시계방향
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    row, col = search()

    print('#{} {}'.format(tc, bfs(row, col)))