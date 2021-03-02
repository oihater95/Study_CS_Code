import sys
sys.setrecursionlimit(100000)  # 재귀 깊이 제한 변경

def dfs(row, col):  #
    global area
    area += 1  # dfs 한 층 내려갈 때마다 넓이(빈 영역 1칸) + 1
    arr[row][col] = 1  # 카운트한 영역은 1로 갱신

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0:
            dfs(nr, nc)

M, N, K = map(int,input().split())
arr = [[0 for _ in range(N)] for i in range(M)]
ans = []  # 각 영역 넓이 리스트

for i in range(K):
    min_col, min_row, max_col, max_row = map(int, input().split())
    for j in range(min_row, max_row):
        for k in range(min_col, max_col):
            arr[j][k] = 1

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            area = 0
            dfs(i, j)
            ans.append(area)

ans = sorted(ans)
print(len(ans))
for area_elem in ans:
    print(area_elem, end = ' ')