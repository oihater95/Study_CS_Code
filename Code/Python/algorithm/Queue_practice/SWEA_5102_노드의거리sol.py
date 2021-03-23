def BFS(sV):
    # 큐 생성과 동시에 선언
    Q = [[sV, 0]]
    visited = [False] * (V+1)  # 방문체크
    visited[sV] = True

    while Q:
        v, dist = Q.pop(0)

        if v == eV:
            return dist

        for i in range(1, V+1):
            if arr[v][i] == 1 and visited[i] == False:
                Q.append([i, dist+1])
                visited[i] = True


def BFS2(sV):
    Q = [sV]
    visited = [False] * (V+1)
    visited[sV] = True
    dist = 0

    while Q:
        size = len(Q)
        for i in range(size):
            v = Q.pop(0)
            if v == eV: return dist

            for i in range(1, V+1):
                if not visited[i] and arr[v][i]:
                    Q.append(i)
                    visited[i] = True


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())  # V: 노드 수, E: 간선 수
    arr = [[0] * (V+1) for _ in range(V+1)]
    Q = []
    # 인접행렬 양방향
    for i in range(E):
        A, B = map(int, input().split())
        arr[A][B] = arr[B][A] = 1

    sV, eV = map(int, input().split())  # 시작점, 도착점

    print('#{} {}'.format(tc, BFS(sV)))