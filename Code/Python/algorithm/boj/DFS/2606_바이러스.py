def dfs(v):
    visited.append(v)
    for i in range(1, N+1):
        if i not in visited and arr[v][i] == 1:
            dfs(i)

    return len(visited) - 1  # 1번 컴퓨터 제외


N = int(input())
M = int(input())

arr = [[0 for _ in range(N+1)] for a in range(N+1)]
visited = []

for i in range(M):
    row, col = map(int, input().split())
    arr[row][col], arr[col][row] = 1, 1  # 인접행렬 양방향

print(dfs(1))  # 1번부터 시작