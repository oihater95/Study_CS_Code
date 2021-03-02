# 작은 수 우선
def DFS(v):  # DFS 재귀
    visited[v] = True  # 방문 => True로 갱신
    path.append(v+1)  # 방문했으니까 경로에 저장

    for i in range(V):
        if adj_arr[v][i] and not visited[i]:  # 연결되어있고 다음꺼 아직 방문 안했다면
            DFS(i)  # return 쓰면 반복문 안돌음, 인접한 노드 중 작은 수 DFS불러옴


T = int(input())

for test_case in range(1, T+1):

    V, E = map(int, input().split())  # 정점 수, 간선 수

    adj_arr = [[0] * V for _ in range(V)]  # 인접 행렬
    visited = [False] * V  # 방문한 노드 확인
    path = []  # 지나온 경로 저장

    for _ in range(E):  # 인접 행렬
        a, b = map(int, input().split())
        adj_arr[a-1][b-1] = 1  # 인덱스가 0부터 시작하기 때문에 -1 방향성 있는 그래프라 adj_arr[b-1][a-1]은 안함

    start, end = map(int, input().split())  # 시작점, 도착점
    DFS(start-1)  # 인덱스는 0부터 시작하기 때문에 -1
    
    # 지나온 경로에 시작점과 끝점 있으면 1, 없으면 0
    # visited[end-1] == True 확인해도 됨
    if start in path and end in path:
        print('#{} {}'.format(test_case, 1))
    else:
        print('#{} {}'.format(test_case, 0))