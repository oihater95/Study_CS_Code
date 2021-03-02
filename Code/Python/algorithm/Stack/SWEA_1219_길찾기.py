def DFS_recursive(v):
    visited[v] = True
    path.append(v)

    for i in range(V):
        if route[v][i] and not visited[i]:  # 인접한 노드 중에 방문하지 않은 곳
            DFS_recursive(i)  # 인접한 노드 중 방문하지 않은 곳부터 다시 길찾기

for test_case in range(1, 11):
    T, N = map(int, input().split())  # test case, 길의 총 개수(간선 수)
    arr = list(map(int, input().split()))
    V = 100  # 노드 수
    route = [[0] * V for _ in range(V)]  # 인접행렬
    visited = [False] * V  # 방문확인
    path = []  # 경로 저장

    for i in range(N):  # 인접행렬, 단방향
        route[arr[2*i]][arr[2*i+1]] = 1

    start, end = 0, 99
    DFS_recursive(start)
    if start in path and end in path:
        print('#{} {}'.format(test_case, 1))
    else:
        print('#{} {}'.format(test_case, 0))