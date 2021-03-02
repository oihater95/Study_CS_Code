# 작은 수 우선
def DFS(v):
    visited[v] = True
    print(chr(v + 65), end=' ')

    for i in range(V):
        if adj_arr[v][i] and not visited[i]:  # 연결되어있고 다음꺼 아직 방문 x
            DFS(i)  # return 쓰면 반복문 안돌음

V, E = map(int, input().split())  # 정점 수, 간선 수

adj_arr = [[0] * V for _ in range(V)]
visited = [False] * V

for _ in range(E):
    a, b = map(int, input().split())
    adj_arr[a][b] = adj_arr[b][a] = 1

DFS(0)