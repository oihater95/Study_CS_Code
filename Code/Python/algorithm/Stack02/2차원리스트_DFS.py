'''
7
0000011
0100100
0110000
0100000
0000000
0111000
0001000
'''


def DFS(r, c):
    global cnt
    cnt += 1
    arr[r][c] = 0  # 방문체크

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:  # 순서는 범위 먼저해야함, 안그러면 인덱스에러날 수 있음
            if arr[nr][nc] == 1:
                DFS(nr, nc)
            else:
                continue


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 0
# 시계방향 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            row = i
            col = j
            cnt = 0
            DFS(row, col)
            print(cnt)

