def bfs(r, c, location_num):
    [r, c, location_num,]

N = int(input())  # 체스판 크기
arr = [list(map(int, input().split())) for _ in range(N)]
location_num = 1  # 1부터 시작

# 나이트, 비숍, 룩 델타 이동 (시계방향)
k_dr = [-2, -1, 1, 2, 2, 1, -1, -2]
k_dc = [1, 2, 2, 1, -1, -2, -2, -1]
b_dr = [-1, 1, 1, -1]
b_dc = [1, 1, -1, -1]
r_dr = [-1, 0, 1, 0]
r_dc = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            row = i
            col = j
            break

bfs(row, col, location_num)

