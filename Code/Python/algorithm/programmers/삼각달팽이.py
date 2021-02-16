n = int(input())
arr = [[0 for i in range(j)] for j in range(1, n + 1)]
num = 1

# down -> right -> up
dr = [1, 0, -1]
dc = [0, 1, -1]
direction = 0  # 0: down, 1: right, 2: up
nr, nc = 0, 0  # 현재 위치

for i in range(1, n * (n + 1) // 2 + 1):
    arr[nr][nc] = i
    if nr + dr[direction%3] > n - 1 or nc + dc[direction%3] > n - 1 or \
            arr[nr + dr[direction%3]][nc + dc[direction%3]] != 0 or nc + dc[direction%3] > n - 1:
        direction += 1
        nr += dr[direction % 3]
        nc += dc[direction % 3]
    else:
        nr += dr[direction % 3]
        nc += dc[direction % 3]

print(arr)