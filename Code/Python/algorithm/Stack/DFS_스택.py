# 큰 수 우선
def DFS(start):
    stack = []
    stack.append(start)

    while stack:
        v = stack.pop()  # 시작점 또는 스택에 있는 노드(인접한 노드)에서 출발
        if not visited[v]:
            visited[v] = True
            print(chr(v+65), end = ' ')
            # 스택이 i가 작은 수부터 쌓이기 때문에 큰 수가 먼저 꺼내진다(LIFO)
            for i in range(V):
                if adj_arr[v][i] and not visited[i]:  # 연결되어있고 다음꺼 아직 방문 x
                    stack.append(i)  # 인접한 노드를 스택에 추가
            
            # 작은 수 우선
            # for i in range(V-1, -1, -1):
            #     if adj_arr[v][i] and not visited[i]:  # 연결되어있고 다음꺼 아직 방문 x
            #         stack.append(i)


V, E = map(int, input().split())  # 정점 수, 간선 수

adj_arr = [[0] * V for _ in range(V)]
visited = [False] * V

for _ in range(E):
    a, b = map(int, input().split())
    adj_arr[a][b] = adj_arr[b][a] = 1

DFS(0)