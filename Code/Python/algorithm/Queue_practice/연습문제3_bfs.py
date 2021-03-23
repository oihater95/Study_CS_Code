'''
입력
8 7
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7
'''

# pop한 후 visited 갱신
def BFS(v):  # v => 탐색 시작점
    queue.append(v)
    while queue:
        print('queue: ', queue)
        temp = queue.pop(0)
        if not visited[temp]:
            visited[temp] = True
        path.append(temp)
        print('visited: ', visited)
        print('path: ', path)

        for i in range(1, N+1):
            if arr[temp][i] and not visited[i] and (i not in queue):  # 인접해있고 아직 방문하지 않은 노드
                queue.append(i)

        print()


def BFS2(v):
    cnt = 0
    queue.append(v)
    visited_dist[v] = cnt
    path.append(v)
    while queue:

        print('queue: ', queue)
        temp = queue.pop(0)
        print('visited: ', visited_dist)
        print('path: ', path)
        cnt += 1

        for i in range(1, N + 1):
            if arr[temp][i] and not visited_dist[i] and (i not in queue):  # 인접해있고 아직 방문하지 않은 노드
                queue.append(i)
                if i not in path:
                    visited_dist[i] = cnt
                    path.append(i)

        print()

G, N = map(int, input().split())  # 간선 수, 노드 수
arr = [[0]*(N+1) for _ in range(N+1)]  # 노드 번호가 1부터 시작
visited = [False] * (N+1)
visited_dist = [0] * (N+1)  # 시작점으로부터의 거리
queue = []
path = []  # 경로

# 인접행렬
for i in range(G):
    A, B = map(int, input().split())
    arr[A][B], arr[B][A] = 1, 1

BFS(1)  # 탐색 시작점: 1
# 새로 초기화
queue = []
path = []
print()
print('#################################')
print()
BFS2(1)  # 탐색 시작점: 1