'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
def BFS(r, c):
   que.append((r, c))
   dist[r][c] = 1

   while que:  # 큐가 빌 때까지
       current = que.pop(0)
       r, c = current[0], current[1]

       for i in range(4):
           nr = r + dr[i]
           nc = c + dc[i]

           if 0 <= nr < N and 0 <= nc < N:
               if arr[nr][nc] == 1 and dist[nr][nc] == 0:
                   que.append((nr, nc))
                   dist[nr][nc] = dist[r][c] + 1




N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 0
dist = [[0] * N for _ in range(N)]  # 시작점으로 부터의 거리
que = []
# 시계방향 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and dist[i][j] == 0:  # 1이고 방문 안한 지점
            row = i
            col = j
            BFS(row, col)

for i in dist:
    print(*i)