# DFS
def DFS(r, c):
    global cnt
    cnt += 1
    arr[r][c] = 0

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 1:
                DFS(nr, nc)



N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
counts = []

# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 시작점
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            row = i
            col = j
            cnt = 0
            DFS(row, col)
            counts.append(cnt)
counts.sort()
print(len(counts))
for i in range(len(counts)):
    print(counts[i])