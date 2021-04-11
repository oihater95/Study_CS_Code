def dfs(r, c):
    global result
    for i in range(4):  # 4방향 탐색
        nr = r + dr[i]
        nc = c + dc[i]
        arr[r][c] = 1  # 지나온 길은 1로 check

        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 3:  # 도착점만나면 result를 1로 갱신
                result = 1
                break

            elif arr[nr][nc] == 0:  # 다음 지점이 0일 경우 해당 지점에서 start
                dfs(nr, nc)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = []
    result = 0

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
    dfs(row, col)
    print('#{} {}'.format(tc, result))