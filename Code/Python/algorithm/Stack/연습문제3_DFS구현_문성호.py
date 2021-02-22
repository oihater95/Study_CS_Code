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

    print(arr)

    for i in range(1, N+1):
        if 1 in arr[i]:
            visited[i] = True
            ans.append(i)
            for j in range(1, N+1):
                if arr[i][j] == 1 and visited[j] == False:
                    s.append(i)
                    v = i
                    break
            break

    print(s, v, visited)

    while s:
        for i in range(v, N+1):
            if arr[v][i] == 1:
                visited[i] == True
                ans.append(i)
                for j in range(v, N+1):
                    if arr[i][j] == 1 and visited[j] == False:
                        s.append(i)
                        v = i
                        print(s, v, visited)
                    else:
                        s.pop()
                        print(s, v, visited)
    print(ans)