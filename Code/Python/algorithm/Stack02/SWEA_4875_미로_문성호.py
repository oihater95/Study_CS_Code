def dfs(r, c):

    for i in range(4):  # 4방향 탐색
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N  and 0 <= nc < N:
            if arr[nr][nc] == 3:
                result = 1
                return result
            elif arr[nr][nc] == 0:
                dfs(nr, nc)
            return


for tc in range(1, int(input())+1):
    N = int(input())
    arr = []
    result = 0
    visited = []
    for i in range(N):  # 미로
        arr.append(list(map(int, input())))

    # 시작점
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                row = i
                col = j
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    print('#{} {}'.format(tc, dfs(row, col)))