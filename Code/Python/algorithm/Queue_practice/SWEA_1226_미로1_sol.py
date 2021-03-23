def DFS(r, c):
    global ans

    if arr[r][c] == 3:  # 도착지점에 도달
        ans = 1
        return

    arr[r][c] = 1  # 방문체크

    for i in range(4):  # 4방향 탐색
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:  # 미로 범위를 벗어나지 않는다면
            if arr[nr][nc] == 0:  # 통로일 경우 해당 지점을 시작점으로 하는 DFS 수행
                DFS(nr, nc)


for tc in range(1, 11):
    t = int(input())
    N = 16
    arr = []
    # 상우하좌 시계방향
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    ans = 0

    for i in range(N):
        arr.append(list(map(int, input())))

    for i in range(N):
        for j in range(N):
            # 시작점 (i, j)
            if arr[i][j] == 2:
                DFS(i, j)

    print('#{} {}'.format(tc, ans))
