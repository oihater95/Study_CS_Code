def BFS(arr):
    cnt = 0
    que = []

    for i in range(N):
        if 0 in arr[i]:
            break
    else:
        return cnt

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                que.append((i, j))
    size = len(que)

    while que:
        for i in range(size):
            temp = que.pop(0)
            row, col = temp[0], temp[1]
            if arr[row][col] == 0:
                arr[row][col] = 1

            for j in range(4):
                nr = row + dr[j]
                nc = col + dc[j]

                if 0 <= nr < N and 0 <= nc < M:
                    if arr[nr][nc] == 0:
                        if (nr, nc) not in que:
                            que.append((nr, nc))
        size = len(que)
        cnt += 1

    for i in range(N):
        if 0 in arr[i]:
            return -1
    else:
        return cnt





M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


print(BFS(arr)-1)
