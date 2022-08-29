from collections import deque

# 최단거리는 bfs로 풀 것

def bfs():
    while q:
        r, c, w = q.popleft()

        if r == n - 1 and c == m - 1:
            return visited[r][c][w]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 0 and visited[nr][nc][w] == 0:  # 벽 부수지 않는 케이스 & 방문 X
                    visited[nr][nc][w] = visited[r][c][w] + 1
                    q.append([nr, nc, w])  # w로 쓰는건 벽 부수기 기회가 0일수도 있고 1일수도 있기 때문
                elif arr[nr][nc] == 1 and w == 1:  # 벽 부수는 케이스
                    visited[nr][nc][0] = visited[r][c][w] + 1
                    q.append([nr, nc, 0])  # 이 이후론 벽 부수기 기회: 0

    return -1


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# [row][col][wall]: 현재까지 이동 거리
# [row][col][0]: 벽 부수기 불가 / [row][col][1]: 벽 부수기 가능
visited[0][0][1] = 1  # 벽을 한번 부술 수 있는 상태에서 시작, 시작 점 카운트 1
q = deque()
q.append([0, 0, 1])
print(bfs())