T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())  # N = 정점수, M = 간선수
    arr = [[0 for _ in range(N+1)] for a in range(N+1)]  # 인덱스와 노드 번호 같게 왼쪽 열 0으로 padding
    visited = [False] * (N+1) # 방문여부
    s = []  # stack
    ans = []

    for i in range(M):
        A, B = map(int, input().split())
        arr[A][B] = 1
        arr[B][A] = 1
    # 시작점 1
    s.append(1)
    visited[1] = True
    v = 1
    print(v, end = ' ')

    while s:
        i = 1
        while i < 8:
            if arr[v][i] == 1 and visited[i] == False:
                visited[i] = True
                s.append(i)
                print(i, end = ' ')
                v = i
            i += 1
        else:
            s.pop()
            if s:
                v = s[-1]

