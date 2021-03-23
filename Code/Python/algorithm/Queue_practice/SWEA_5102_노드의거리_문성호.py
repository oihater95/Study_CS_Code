def BFS(v):
    global cnt
    que.append(v)
    visited[v] = cnt
    while que:
        size = len(que)

        for s in range(size):  # 거리 같은 노드 묶어서 처리
            temp = que.pop(0)
            visited[temp] = cnt

            if temp == G:  # 도착지점 방문
                return cnt

            for i in range(V):
                if arr[temp][i] == 1 and visited[i] == -1:  # 연결되어있고 아직 방문하지 않았다면 큐에 추가
                    que.append(i)
        cnt += 1

    if visited[G] == -1:  # 도달하지 못하면 0
        return 0


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())  # V: 노드 수, E: 간선 수
    arr = [[0] * V for _ in range(V)]
    visited = [-1] * V
    que = []
    cnt = 0
    # 인접행렬 양방향
    for i in range(E):
        A, B = map(int, input().split())
        arr[A-1][B-1] = arr[B-1][A-1] = 1  # 노드 번호는 1부터 시작, 인덱스는 0부터 시작

    S, G = map(int, input().split())  # S: 시작점, G: 도착점
    S -= 1
    G -= 1

    print('#{} {}'.format(tc, BFS(S)))