from collections import deque

def bfs(s, c):
    global min_cnt
    que = deque()
    que.append((s, c))

    while que:
        start, cnt = que.popleft()

        for next in adj[start]:
            if next == b:
                cnt += 1
                if min_cnt > cnt:
                    min_cnt = cnt
                    return min_cnt

            if visited[next] == False and next != 0:
                visited[next] = True
                que.append((next, cnt+1))

    min_cnt = -1
    return min_cnt


a, b = map(int, input().split())
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
min_cnt = 987654321
visited = [False] * (N+1)

for i in range(M):  # 인접리스트
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

if a != b:
    visited[a] = True
    min_cnt = bfs(a, 0)

else:
    min_cnt = 0

print(min_cnt)