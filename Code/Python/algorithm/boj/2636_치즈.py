from collections import deque

def bfs():
    visited = [[False] * m for _ in range(n)]

    q = deque()
    q.append([0, 0])
    visited[0][0] = True
    cnt = 0

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == False:
                if arr[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append([nr, nc])
                else:
                    arr[nr][nc] = 0
                    cnt += 1
                    visited[nr][nc] = True

    cheeses.append(cnt)
    return cnt

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cheeses = []  # 남은 치즈
time = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    time += 1
    cnt = bfs()
    if cnt == 0:
        break

print(time-1)
print(cheeses[-2])